import reflex as rx
from finance_app.data.models import ArticleData

def article_player(article: ArticleData) -> rx.Component:
    category_colors = {
        "Credit": "bg-amber-100 text-amber-800 border-amber-300",
        "Investing": "bg-emerald-100 text-emerald-800 border-emerald-300",
        "Savings": "bg-rose-100 text-rose-800 border-rose-300",
    }
    badge_style = category_colors.get(article.category, "bg-slate-100 text-slate-800")

    return rx.box(
        # Header / Hero Section
        rx.box(
            rx.box(
                rx.center(
                    rx.text(f"{{{article.head_image_label}}}", class_name="text-slate-400 text-sm"),
                    class_name="w-full h-full"
                ),
                class_name="w-full h-[320px] bg-stone-500"
            ),
            rx.center(
                rx.vstack(
                    rx.badge(f"🌱 {article.category} • {article.read_time}", class_name=f"px-3 py-1 rounded-full text-xs font-bold border {badge_style}"),
                    rx.heading(article.title, class_name="text-3xl md:text-5xl font-bold text-white text-center drop-shadow-md max-w-2xl px-4"),
                    class_name="items-center space-y-3"
                ),
                class_name="absolute inset-0 flex items-center justify-center p-4 bg-black/20"
            ),
            class_name="relative w-full"
        ),

        # Content Body
        rx.vstack(
            rx.text(article.intro_text, class_name="text-base text-stone-800 leading-relaxed text-justify"),
            rx.box(
                rx.box(
                    rx.center(rx.text(f"{{{article.paragraph_photo_label}}}", class_name="text-slate-400 text-xs text-center px-2"), class_name="w-full h-full"),
                    class_name="w-full md:w-1/2 h-[220px] bg-stone-400 shrink-0 rounded-xl"
                ),
                rx.text(article.mid_text, class_name="w-full md:w-1/2 text-base text-stone-800 leading-relaxed text-justify"),
                class_name="flex flex-col md:flex-row gap-6 items-start w-full my-4"
            ),
            rx.text(article.closing_text, class_name="text-base text-stone-800 leading-relaxed text-justify"),
            rx.divider(class_name="border-stone-300 border-t my-6 w-full"),
            rx.vstack(
                rx.text(article.author_info, class_name="text-sm font-semibold text-stone-600"),
                rx.vstack(*[rx.link(src, href=src, is_external=True, class_name="text-xs text-emerald-700 hover:underline") for src in article.sources], class_name="space-y-1 mt-2"),
                class_name="align-start w-full"
            ),
            class_name="max-w-3xl mx-auto px-6 py-8 space-y-6"
        ),
        class_name="w-full min-h-screen bg-white"
    )