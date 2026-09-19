import reflex as rx
from finance_app.state.habitat_state import HabitatState


def cloud_rain_overlay() -> rx.Component:
    """Renders a single cloud that toggles between ☁️ and 🌧️ every 0.5s ONLY when is_raining is True."""
    return rx.cond(
        HabitatState.is_raining,
        rx.box(
            rx.box(
                class_name="text-6xl md:text-7xl dynamic-cloud-emoji animate-cloud-toggle transition-all duration-300 drop-shadow-lg",
            ),
            class_name="absolute top-[12%] left-1/2 -translate-x-1/2 z-30 pointer-events-none flex justify-center items-center",
        ),
        # Render empty box when not raining (hidden on launch)
        rx.box(),
    )

def sparkle_overlay() -> rx.Component:
    """Renders larger floating sparkles around the flower during a Level-Up celebration."""
    return rx.box(
        rx.text(
            "✨",
            class_name="absolute top-[20%] left-[28%] text-4xl md:text-5xl animate-sparkle-1 z-30 drop-shadow-md",
        ),
        rx.text(
            "🌟",
            class_name="absolute top-[18%] right-[28%] text-5xl md:text-6xl animate-sparkle-2 z-30 drop-shadow-md",
        ),
        rx.text(
            "✨",
            class_name="absolute bottom-[30%] left-[30%] text-4xl md:text-5xl animate-sparkle-3 z-30 drop-shadow-md",
        ),
        rx.text(
            "⭐",
            class_name="absolute bottom-[25%] right-[30%] text-4xl md:text-5xl animate-sparkle-4 z-30 drop-shadow-md",
        ),
        class_name="absolute inset-0 pointer-events-none z-30 flex items-center justify-center",
    )


def habitat_component() -> rx.Component:
    """Primary Visual Growth Habitat component embedded in the Dashboard."""
    return rx.vstack(
        # --- 1. Savings Header Display ---
        rx.vstack(
            rx.text(
                "Rainy Day Savings",
                class_name="text-xs uppercase tracking-widest text-[#064E3B] font-bold",
            ),
            rx.heading(
                f"${HabitatState.savings_balance:.2f}",
                class_name="text-4xl font-black text-[#064E3B]",
            ),
            class_name="items-center space-y-1 w-full pt-2",
        ),
        # --- 2. Flower Habitat Center ---
        rx.box(
            # Single Alternating Rain Cloud Overlay
            cloud_rain_overlay(),
            # Level Up Sparkle Celebration Overlay
            rx.cond(HabitatState.show_sparkles, sparkle_overlay()),
            # Plant Vector Asset
            rx.image(
                src=HabitatState.current_image,
                alt="Plant Growth Stage",
                class_name="w-full h-full max-h-[380px] object-contain transition-transform duration-500 hover:scale-105 z-10 relative drop-shadow-sm",
            ),
            class_name="relative flex-1 flex items-center justify-center w-full min-h-[320px] my-2",
        ),
        # --- 3. Action Deposit Buttons ---
        rx.hstack(
            rx.button(
                "🌱 +$5 Deposit",
                on_click=HabitatState.add_savings(5.00),
                class_name="flex-1 bg-[#064E3B] hover:bg-[#FB923C] text-[#FAFAF9] font-bold py-3.5 px-4 rounded-none shadow-none border border-[#064E3B] transition-colors active:scale-95 text-xs uppercase tracking-wider cursor-pointer",
            ),
            rx.button(
                "🌸 +$20 Deposit",
                on_click=HabitatState.add_savings(20.00),
                class_name="flex-1 bg-[#FB923C] hover:bg-[#064E3B] text-[#FAFAF9] font-bold py-3.5 px-4 rounded-none shadow-none border border-[#064E3B] transition-colors active:scale-95 text-xs uppercase tracking-wider cursor-pointer",
            ),
            class_name="w-full space-x-3 pt-2",
        ),
        class_name="w-full max-w-md h-[560px] mx-auto p-6 bg-[#FAFAF9] border-2 border-[#EAB308] rounded-none flex flex-col justify-between items-center shadow-none",
    )