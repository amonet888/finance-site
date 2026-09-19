import reflex as rx
from finance_app.data.content import ALL_ARTICLES
from finance_app.pages.habitat import habitat_component

def test_index_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            # Header Section
            rx.heading("🧪 Hackathon Testing Hub", class_name="text-3xl font-bold text-slate-800"),
        
            # Interactive Plant Habitat Section
            habitat_component(),
            rx.divider(class_name="my-6 border-slate-300 w-full"),

            # Dynamic Article Links Container
            rx.text("Click any lesson below to test the dynamic article player layout:", class_name="text-slate-600 mb-4"),
            rx.vstack(
                *[
                    rx.link(
                        rx.box(
                            rx.hstack(
                                rx.vstack(
                                    rx.badge(article.category, class_name="w-fit text-xs px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold"),
                                    rx.text(article.title, class_name="text-lg font-bold text-slate-900"),
                                    rx.text(f"ID: {article.id} • {article.read_time}", class_name="text-xs text-slate-500"),
                                    class_name="align-start space-y-1"
                                ),
                                rx.text("➡️", class_name="text-xl"),
                                class_name="justify-between items-center w-full"
                            ),
                            class_name="w-full p-4 bg-white rounded-xl shadow-md border border-slate-200 hover:border-emerald-500 hover:shadow-lg transition-all cursor-pointer"
                        ),
                        href=f"/learn/{article.id}",
                        class_name="w-full"
                    )
                    for article in ALL_ARTICLES
                ],
                class_name="w-full space-y-3"
            ),
            class_name="w-full max-w-lg p-6 bg-slate-50 rounded-2xl shadow-sm border border-slate-200 space-y-4"
        ),
        class_name="min-h-screen bg-slate-100 p-6"
    )