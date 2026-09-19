import asyncio
import reflex as rx

class HabitatState(rx.State):
    # --- Core State Variables ---
    growth_xp: int = 0
    savings_balance: float = 350.00          # Initial starting balance
    emergency_target: float = 300.00         # Target threshold to be "Healthy"
    is_raining: bool = False
    show_sparkles: bool = False

    # --- Computed Properties ---
    @rx.var
    def plant_stage(self) -> int:
        """Determines growth stage (0 through 3) based on 50 XP increments."""
        if self.growth_xp >= 150:
            return 3
        elif self.growth_xp >= 100:
            return 2
        elif self.growth_xp >= 50:
            return 1
        return 0

    @rx.var
    def is_healthy(self) -> bool:
        """Plant is healthy (1) if savings meet or exceed safety target, otherwise weak (0)."""
        return self.savings_balance >= self.emergency_target

    @rx.var
    def current_image(self) -> str:
        """
        Dynamically constructs PNG asset path:
        - Stage 0: Always defaults to /state_00.png (starting seed)
        - Stage 1-3: Dynamically swaps based on health (state_1X vs state_0X)
        """
        # Stage 0 is always state_00.png
        if self.plant_stage == 0:
            return "/state_00.png"
        
        # Stages 1, 2, and 3 swap between Healthy (1) and Weak (0)
        health_prefix = "1" if self.is_healthy else "0"
        return f"/state_{health_prefix}{self.plant_stage}.png"


    @rx.var
    def cushion_percentage(self) -> float:
        """Calculates cushion progress percentage bounded between 0 and 100."""
        if self.emergency_target <= 0:
            return 0.0
        pct = (self.savings_balance / self.emergency_target) * 100.0
        return max(0.0, min(100.0, pct))

    @rx.var
    def gardener_rank(self) -> str:
        """Returns dynamic gardener rank based on current plant stage."""
        ranks = [
            "🌱 Level 1 Seedling",
            "🌿 Level 2 Sprout",
            "🌺 Level 3 Budding",
            "👑 Level 4 Master Gardener",
        ]
        return ranks[min(self.plant_stage, 3)]

    # --- Action Handlers ---
    def add_savings(self, amount: float):
        """Adds to savings balance and turns on rain shower."""
        self.savings_balance += amount
        self.is_raining = True

    def sim_impulse_spend(self, amount: float):
        """
        Drains savings balance. If balance drops below target ($300),
        is_healthy becomes False (shifting current_image to state_0X.png).
        """
        if self.savings_balance >= amount:
            self.savings_balance -= amount
        else:
            self.savings_balance = 0.0
            
        # Stop rain if balance drops below target
        if not self.is_healthy:
            self.is_raining = False

    def sim_deposit_cushion(self, amount: float):
        """Replenishes savings balance and triggers rain animation."""
        self.savings_balance += amount
        self.is_raining = True

    async def trigger_level_up_effects(self):
        """Triggers sparkle animation and pops a site notification."""
        self.show_sparkles = True
        yield rx.toast.success(
            "🎉 YOU HAVE LEVELED UP! Your habitat is flourishing!",
            position="top-center",
            duration=4000,
            style={
                "background_color": "#064E3B",
                "color": "#FAFAF9",
                "border": "2px solid #EAB308",
                "border_radius": "0px",
                "font_weight": "bold"
            }
        )
        await asyncio.sleep(3.5)
        self.show_sparkles = False