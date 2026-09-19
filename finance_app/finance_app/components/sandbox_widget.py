import reflex as rx
from finance_app.state.habitat_state import HabitatState

def impulse_sandbox_widget() -> rx.Component:
    return rx.box(
        rx.vstack(
            # --- Header ---
            rx.hstack(
                rx.hstack(
                    rx.text("🛡️", class_name="text-lg"),
                    rx.heading(
                        "Emergency Shield Simulator", 
                        class_name="text-md font-bold text-[#064E3B]"
                    ),
                    class_name="items-center space-x-1.5"
                ),
                rx.badge(
                    "HEALTH ENGINE", 
                    class_name="bg-[#FB923C] text-[#FAFAF9] rounded-none text-[10px] font-bold px-2 py-0.5"
                ),
                class_name="justify-between items-center w-full border-b border-[#064E3B] pb-2"
            ),

            # --- Target Status & Indicator ---
            rx.hstack(
                rx.vstack(
                    rx.text("Current Shield Cushion", class_name="text-xs text-[#064E3B] font-semibold"),
                    rx.heading(
                        f"${HabitatState.savings_balance:.2f} / ${HabitatState.emergency_target:.2f}",
                        class_name="text-lg font-black text-[#064E3B]"
                    ),
                    class_name="align-start space-y-0"
                ),
                # Dynamic Health Badge
                rx.cond(
                    HabitatState.is_healthy,
                    rx.badge(
                        "💚 HEALTHY SOIL",
                        class_name="bg-[#064E3B] text-[#FAFAF9] font-bold rounded-none text-xs px-2.5 py-1"
                    ),
                    rx.badge(
                        "🥀 WILTED / WEAK",
                        class_name="bg-[#FB923C] text-[#FAFAF9] font-bold rounded-none text-xs px-2.5 py-1 animate-pulse"
                    )
                ),
                class_name="justify-between items-center w-full pt-1"
            ),

            # --- Visual Cushion Progress Bar ---
            rx.box(
                rx.box(
                    class_name="h-full transition-all duration-500 rounded-none",
                    style={
                        "width": f"{HabitatState.cushion_percentage}%",
                        "background_color": rx.cond(HabitatState.is_healthy, "#064E3B", "#FB923C")
                    }
                ),
                class_name="w-full bg-[#FAFAF9] h-3 border border-[#064E3B] rounded-none overflow-hidden my-1"
            ),

            # --- Interactive Decision Controls ---
            rx.vstack(
                rx.text(
                    "Simulate Real-World Scenarios:", 
                    class_name="text-xs font-bold text-[#064E3B] uppercase tracking-wider"
                ),
                rx.grid(
                    # Scenario A: Impulse Purchase (Drains health below target)
                    rx.button(
                        "🛍️ Buy $120 Concert Ticket",
                        on_click=HabitatState.sim_impulse_spend(120.00),
                        class_name="bg-[#FAFAF9] hover:bg-[#FB923C] hover:text-[#FAFAF9] text-[#064E3B] font-bold text-xs py-2 px-3 border border-[#064E3B] rounded-none transition-colors cursor-pointer text-left w-full"
                    ),
                    # Scenario B: Emergency Shock (Drains health significantly)
                    rx.button(
                        "🚨 $180 Urgent Dental Bill",
                        on_click=HabitatState.sim_impulse_spend(180.00),
                        class_name="bg-[#FAFAF9] hover:bg-[#FB923C] hover:text-[#FAFAF9] text-[#064E3B] font-bold text-xs py-2 px-3 border border-[#064E3B] rounded-none transition-colors cursor-pointer text-left w-full"
                    ),
                    # Scenario C: Deposit/Restore Health (Raises balance above target)
                    rx.button(
                        "💧 Replenish Cushion (+$100)",
                        on_click=HabitatState.sim_deposit_cushion(100.00),
                        class_name="bg-[#064E3B] hover:bg-[#EAB308] hover:text-[#064E3B] text-[#FAFAF9] font-bold text-xs py-2 px-3 border border-[#064E3B] rounded-none transition-colors cursor-pointer text-left w-full col-span-2"
                    ),
                    class_name="grid grid-cols-2 gap-2 w-full"
                ),
                class_name="w-full space-y-1.5 pt-1"
            ),

            # --- Live Feedback Note ---
            rx.cond(
                HabitatState.is_healthy,
                rx.text(
                    "✨ Cushion is fully funded ($300+ target). Your plant is strong and healthy!",
                    class_name="text-[11px] text-[#064E3B] font-medium italic"
                ),
                rx.text(
                    "⚠️ Savings are below safety target! Your flower has wilted into its weak state.",
                    class_name="text-[11px] text-[#FB923C] font-bold italic"
                )
            ),

            class_name="space-y-3 w-full"
        ),
        class_name="bg-[#FFEDD5] border-2 border-[#064E3B] p-5 rounded-none w-full shadow-none"
    )