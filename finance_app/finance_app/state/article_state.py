import reflex as rx
from finance_app.state.habitat_state import HabitatState

class ArticleState(rx.State):
    current_step: int = 0
    max_steps: int = 2

    def next_step(self):
        if self.current_step < self.max_steps:
            self.current_step += 1

    def prev_step(self):
        if self.current_step > 0:
            self.current_step -= 1

    async def complete_lesson_and_return(self):
        """Awards +50 XP, triggers level up effects if stage changed, and redirects to Dashboard."""
        # 1. Fetch HabitatState instance using await
        habitat = await self.get_state(HabitatState)
        
        # 2. Capture the current plant stage BEFORE adding XP
        old_stage = habitat.plant_stage
        
        # 3. Add 50 XP to trigger stage recalculation
        habitat.growth_xp += 50
        
        # 4. Reset article reader index
        self.current_step = 0
        
        # 5. Compare new stage to old_stage
        if habitat.plant_stage > old_stage:
            return [
                HabitatState.trigger_level_up_effects,
                rx.redirect("/")
            ]

        # 6. Redirect back to Dashboard if no level-up occurred
        return rx.redirect("/")