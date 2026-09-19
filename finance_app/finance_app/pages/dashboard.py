import reflex as rx
from finance_app.components import impulse_sandbox_widget
from finance_app.data.content import ALL_ARTICLES
from finance_app.pages.habitat import habitat_component
from finance_app.state.habitat_state import HabitatState


def dashboard_page() -> rx.Component:
    return rx.box(
        # --- Top Navigation Bar ---
        rx.hstack(
            rx.hstack(
                rx.text("🌸", class_name="text-2xl"),
                rx.heading(
                    "SproutFinance",
                    class_name="text-2xl font-black tracking-tight text-[#FAFAF9]",
                ),
                class_name="items-center space-x-2",
            ),
            # Gardener Badge (Streak removed, rank updates dynamically with plant stage)
            rx.badge(
                HabitatState.gardener_rank,
                class_name="bg-[#EAB308] text-[#064E3B] font-bold px-4 py-1.5 rounded-none text-xs uppercase tracking-wider border border-[#FAFAF9]",
            ),
            class_name="w-full justify-between items-center px-8 py-4 bg-[#064E3B] border-b-2 border-[#FB923C]",
        ),
        # --- Main Dashboard Content Area ---
        rx.box(
            rx.grid(
                # --- Left Column: Visual Ecosystem Container ---
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "Visual Ecosystem",
                            class_name="text-xl font-bold text-[#FAFAF9] border-b-2 border-[#EAB308] pb-1 w-full",
                        ),
                        # Embedded Habitat Component (Inner box holding the flower remains cream/white)
                        habitat_component(),
                        rx.text(
                            "Your financial habits are keeping your ecosystem healthy and resilient!",
                            class_name="text-sm italic text-center text-[#FAFAF9] font-medium mt-2",
                        ),
                        class_name="space-y-4 w-full items-center",
                    ),
                    # Outer ecosystem container styled in dark green (#064E3B)
                    class_name="bg-[#064E3B] border-2 border-[#064E3B] p-6 rounded-none shadow-none w-full",
                ),
                # --- Right Column: Simulation & Action Hub ---
                rx.vstack(
                    impulse_sandbox_widget(),
                    # Fast Financial Metrics
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                "📈 Fast Financial Sandboxes",
                                class_name="text-lg font-bold text-[#064E3B]",
                            ),
                            rx.hstack(
                                rx.vstack(
                                    rx.text(
                                        "Credit Score Projection",
                                        class_name="text-xs text-[#064E3B] font-semibold",
                                    ),
                                    rx.text(
                                        "720 (+15 pts)",
                                        class_name="text-xl font-black text-[#064E3B]",
                                    ),
                                    class_name="p-3 bg-[#FAFAF9] border border-[#064E3B] rounded-none flex-1",
                                ),
                                rx.vstack(
                                    rx.text(
                                        "5-Yr Compound Yield",
                                        class_name="text-xs text-[#064E3B] font-semibold",
                                    ),
                                    rx.text(
                                        "$1,280 projected",
                                        class_name="text-xl font-black text-[#EAB308]",
                                    ),
                                    class_name="p-3 bg-[#FAFAF9] border border-[#064E3B] rounded-none flex-1",
                                ),
                                class_name="w-full space-x-3",
                            ),
                            class_name="space-y-3 w-full",
                        ),
                        class_name="bg-[#FAFAF9] border-2 border-[#064E3B] p-5 rounded-none w-full",
                    ),
                    class_name="space-y-6 w-full",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 gap-8 w-full max-w-7xl mx-auto",
            ),
            # --- Bottom Row: Educational Modules Grid ---
            rx.box(
                rx.vstack(
                    rx.heading(
                        "📚 Recommended Modules For Growth",
                        class_name="text-xl font-bold text-[#064E3B] border-b-2 border-[#FB923C] pb-1 w-full",
                    ),
                    rx.grid(
                        *[
                            rx.link(
                                rx.box(
                                    rx.vstack(
                                        rx.badge(
                                            article.category,
                                            class_name="bg-[#064E3B] text-[#FAFAF9] text-[10px] font-bold rounded-none px-2 py-0.5",
                                        ),
                                        rx.text(
                                            article.title,
                                            class_name="text-md font-bold text-[#064E3B] line-clamp-1",
                                        ),
                                        rx.text(
                                            f"{article.read_time} • +50 Growth XP",
                                            class_name="text-xs font-semibold text-[#FB923C]",
                                        ),
                                        class_name="align-start space-y-1.5",
                                    ),
                                    class_name="bg-[#FAFAF9] border-2 border-[#064E3B] p-4 rounded-none hover:bg-[#FFEDD5] transition-colors cursor-pointer h-full",
                                ),
                                href=f"/learn/{article.id}",
                                class_name="w-full",
                            )
                            for article in ALL_ARTICLES
                        ],
                        class_name="grid grid-cols-1 md:grid-cols-3 gap-4 w-full pt-2",
                    ),
                    class_name="space-y-4 w-full",
                ),
                class_name="w-full max-w-7xl mx-auto mt-8 p-6 bg-[#FAFAF9] border-2 border-[#064E3B] rounded-none",
            ),
            class_name="p-8 w-full",
        ),
        class_name="min-h-screen bg-[#FAFAF9] font-sans",
    )