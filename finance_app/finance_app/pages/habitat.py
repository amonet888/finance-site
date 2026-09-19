import reflex as rx
from finance_app.state.habitat_state import HabitatState

def advanced_rain_shower() -> rx.Component:
    return rx.box(
        # --- Overlapping Clouds ---
        rx.box(
            rx.image(
                src="/cloud_1.png",
                class_name="w-20 h-auto absolute left-0 top-0 z-20"
            ),
            rx.image(
                src="/cloud_2.png",
                class_name="w-24 h-auto absolute left-8 -top-3 z-30"
            ),
            class_name="relative w-36 h-12 animate-cloud-float mx-auto"
        ),

        # --- Falling Raindrops Container ---
        # Fixed height allows drops to travel down over the flower without pushing other elements
        rx.box(
            rx.image(src="/raindrop.png", class_name="w-3 h-auto absolute left-[10%] top-0 animate-drop-1"),
            rx.image(src="/raindrop.png", class_name="w-2.5 h-auto absolute left-[30%] top-0 animate-drop-2"),
            rx.image(src="/raindrop.png", class_name="w-3.5 h-auto absolute left-[50%] top-0 animate-drop-3"),
            rx.image(src="/raindrop.png", class_name="w-2.5 h-auto absolute left-[70%] top-0 animate-drop-4"),
            rx.image(src="/raindrop.png", class_name="w-3 h-auto absolute left-[88%] top-0 animate-drop-5"),
            class_name="absolute top-8 inset-x-0 h-64 pointer-events-none z-20"
        ),
        
        # Absolute position floating higher than the flower container
        class_name="absolute -top-12 inset-x-0 flex flex-col items-center justify-center z-30 w-full pointer-events-none"
    )

def habitat_component() -> rx.Component:
    return rx.vstack(
        # --- 1. Top Section: Savings Display ---
        rx.vstack(
            rx.text(
                "Rainy Day Savings", 
                class_name="text-xs uppercase tracking-widest text-emerald-700 font-bold"
            ),
            rx.heading(
                f"${HabitatState.savings_balance:.2f}", 
                class_name="text-4xl font-extrabold text-stone-800"
            ),
            class_name="items-center space-y-1 w-full pt-2"
        ),

        # --- 2. Center Section: Prominent Flower Hero ---
        rx.box(
            # Dynamic Rain System Overlay
            rx.cond(
                HabitatState.is_raining,
                advanced_rain_shower()
            ),
            
            # Expanded Flower Vector (Maximized size while preserving aspect ratio)
            rx.image(
                src=HabitatState.current_image,
                alt="Plant Growth Stage",
                class_name="w-full h-full max-h-[380px] object-contain transition-transform duration-500 hover:scale-105 z-10 relative drop-shadow-sm"
            ),
            class_name="relative flex-1 flex items-center justify-center w-full min-h-[320px] my-2"
        ),

        # --- 3. Bottom Section: Action Deposit Buttons ---
        rx.hstack(
            rx.button(
                "🌱 +$5 Deposit", 
                on_click=HabitatState.add_savings(5.00),
                class_name="flex-1 bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3.5 px-4 rounded-2xl shadow-md transition-all active:scale-95 text-base"
            ),
            rx.button(
                "🌸 +$20 Deposit", 
                on_click=HabitatState.add_savings(20.00),
                class_name="flex-1 bg-rose-500 hover:bg-rose-600 text-white font-bold py-3.5 px-4 rounded-2xl shadow-md transition-all active:scale-95 text-base"
            ),
            class_name="w-full space-x-3 pt-2"
        ),
        
        # Outer Card Container (Expanded height & padded edges)
        class_name="w-full max-w-md h-[600px] mx-auto p-6 bg-stone-50 border border-stone-200 rounded-3xl flex flex-col justify-between items-center shadow-lg"
    )