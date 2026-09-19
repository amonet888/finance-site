import reflex as rx
from finance_app.data.models import ArticleData
from finance_app.state.article_state import ArticleState

def article_player(article: ArticleData) -> rx.Component:
    return rx.box(
        # --- Top Navigation Bar ---
        rx.hstack(
            rx.link(
                rx.button(
                    "← Back to Dashboard",
                    class_name="bg-[#FAFAF9] text-[#064E3B] hover:bg-[#FFEDD5] font-bold text-xs uppercase tracking-wider py-2 px-4 border border-[#064E3B] rounded-none cursor-pointer"
                ),
                href="/"
            ),
            rx.text(
                f"Section {ArticleState.current_step + 1} of 3",
                class_name="text-xs font-bold text-[#064E3B] uppercase tracking-wider bg-[#FFEDD5] px-3 py-1 border border-[#064E3B]"
            ),
            rx.badge(
                article.category,
                class_name="bg-[#FB923C] text-[#FAFAF9] font-bold text-xs uppercase tracking-wider py-1 px-3 rounded-none"
            ),
            class_name="w-full justify-between items-center max-w-3xl mx-auto mb-6"
        ),

        # --- Progress Bar ---
        rx.box(
            rx.box(
                class_name="bg-[#EAB308] h-full transition-all duration-500",
                style={"width": f"{((ArticleState.current_step + 1) / 3) * 100}%"}
            ),
            class_name="w-full max-w-3xl mx-auto bg-[#FFEDD5] h-2 border border-[#064E3B] mb-6 rounded-none overflow-hidden"
        ),

        # --- Animated Dynamic Content Card ---
        rx.box(
            rx.vstack(
                # Title Header
                rx.vstack(
                    rx.heading(
                        article.title, 
                        class_name="text-2xl md:text-3xl font-black text-[#064E3B] leading-tight"
                    ),
                    rx.text(f"⏱️ {article.read_time} • {article.author_info}", class_name="text-xs font-bold text-[#FB923C] uppercase tracking-wider"),
                    class_name="w-full border-b-2 border-[#EAB308] pb-4 space-y-1"
                ),

                # STEP 0: INTRO
                rx.cond(
                    ArticleState.current_step == 0,
                    rx.vstack(
                        rx.box(
                            rx.text(article.intro_text, class_name="text-lg text-[#064E3B] font-medium leading-relaxed"),
                            class_name="w-full bg-[#FFEDD5] border-l-4 border-[#FB923C] p-5 rounded-none"
                        ),
                        rx.box(
                            rx.vstack(
                                rx.text("🌸 Visual Learning Graphic", class_name="text-xs uppercase tracking-widest font-bold text-[#FAFAF9]"),
                                rx.text(article.head_image_label, class_name="text-md font-bold text-[#FAFAF9] text-center"),
                                class_name="items-center justify-center h-40 w-full p-4"
                            ),
                            class_name="w-full bg-[#064E3B] border-2 border-[#064E3B] rounded-none"
                        ),
                        class_name="w-full space-y-4 animate-slide-up"
                    )
                ),

                # STEP 1: MAIN BODY
                rx.cond(
                    ArticleState.current_step == 1,
                    rx.vstack(
                        rx.text(article.mid_text, class_name="text-base text-[#064E3B] leading-relaxed"),
                        rx.box(
                            rx.text(f"📊 Diagram: {article.paragraph_photo_label}", class_name="text-sm font-bold text-[#064E3B] text-center"),
                            class_name="w-full bg-[#FAFAF9] border-2 border-[#064E3B] p-6 rounded-none"
                        ),
                        class_name="w-full space-y-4 animate-slide-up"
                    )
                ),

                # STEP 2: CLOSING & CLAIM XP
                rx.cond(
                    ArticleState.current_step == 2,
                    rx.vstack(
                        rx.text(article.closing_text, class_name="text-base text-[#064E3B] leading-relaxed"),
                        rx.box(
                            rx.vstack(
                                rx.heading("🎉 Lesson Complete!", class_name="text-lg font-bold text-[#064E3B]"),
                                rx.text("Claim your Growth XP to level up your plant habitat stage on the dashboard.", class_name="text-xs text-[#064E3B]"),
                                rx.button(
                                    "🌱 Complete Lesson (+50 Growth XP)",
                                    on_click=ArticleState.complete_lesson_and_return,
                                    class_name="bg-[#FB923C] hover:bg-[#064E3B] text-[#FAFAF9] font-bold text-sm py-3 px-6 rounded-none border border-[#064E3B] transition-colors w-full cursor-pointer active:scale-95"
                                ),
                                class_name="items-center space-y-3 w-full"
                            ),
                            class_name="w-full bg-[#FFEDD5] border-2 border-[#064E3B] p-6 rounded-none"
                        ),
                        class_name="w-full space-y-4 animate-slide-up"
                    )
                ),

                # Interactive Controls (Prev / Next)
                rx.hstack(
                    rx.button(
                        "← Previous",
                        on_click=ArticleState.prev_step,
                        is_disabled=ArticleState.current_step == 0,
                        class_name="bg-[#FAFAF9] text-[#064E3B] border border-[#064E3B] font-bold text-xs py-2.5 px-5 rounded-none disabled:opacity-40 cursor-pointer"
                    ),
                    rx.cond(
                        ArticleState.current_step < ArticleState.max_steps,
                        rx.button(
                            "Next Section →",
                            on_click=ArticleState.next_step,
                            class_name="bg-[#064E3B] hover:bg-[#FB923C] text-[#FAFAF9] font-bold text-xs py-2.5 px-5 rounded-none transition-colors cursor-pointer"
                        ),
                        # On final slide, "Next Section" disappears completely so the user focuses on "Complete Lesson"
                        rx.box()
                    ),
                    class_name="w-full justify-between pt-6 border-t border-[#064E3B] mt-4"
                ),
                class_name="space-y-6 w-full"
            ),
            class_name="w-full max-w-3xl mx-auto bg-[#FAFAF9] border-2 border-[#064E3B] p-8 rounded-none shadow-none"
        ),
        class_name="min-h-screen bg-[#FAFAF9] p-6 font-sans"
    )