import asyncio
import reflex as rx

class HabitatState(rx.State):
    savings_balance: float = 0.00
    plant_stage: int = 0  # Indexes 0 through 3 (4 vector stages)
    is_raining: bool = False

    # Image mapping matching your assets folder
    stage_images: list[str] = [
        "/stage_0.png",  # Seed in soil
        "/stage_1.png",  # Sprout with leaves
        "/stage_2.png",  # Rosebud
        "/stage_3.png",  # Full Bloom
    ]

    @rx.var
    def current_image(self) -> str:
        return self.stage_images[min(self.plant_stage, len(self.stage_images) - 1)]

    async def add_savings(self, amount: float):
        self.savings_balance += amount
        
        # Trigger rain cloud animation
        self.is_raining = True
        yield  # Push rain update to UI instantly
        
        # Let rain fall for 1.5 seconds
        await asyncio.sleep(1.5)
        
        # Advance growth stage if not fully bloomed
        if self.plant_stage < len(self.stage_images) - 1:
            self.plant_stage += 1
            
        # Hide rain cloud
        self.is_raining = False