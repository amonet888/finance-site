import reflex as rx
from finance_app.data.content import ALL_ARTICLES
from finance_app.pages.article_player import article_player
from finance_app.pages.dashboard import dashboard_page  # Import Dashboard
from finance_app.pages.test_index import test_index_page  # Keep testing page for backup
from finance_app.components.sandbox_widget import impulse_sandbox_widget

app = rx.App()

# Set the Dashboard as the primary homepage (route="/")
app.add_page(
    dashboard_page, 
    route="/", 
    title="SproutFinance | Dashboard"
)

# Keep the Testing Hub accessible at /test for quick debugging
app.add_page(
    test_index_page, 
    route="/test", 
    title="Testing Hub"
)

# --- Right Column: Simulation & Action Hub ---
rx.vstack(
    # Integrated Health Sandbox Widget
    impulse_sandbox_widget(),

    # Fast Financial Metrics / Sandboxes
    # ...
    class_name="space-y-6 w-full"
)

# Helper function to create a page renderer for a specific article
def make_article_page(selected_article):
    return lambda: article_player(selected_article)

# Register routes cleanly without lambda parameter warnings
for article in ALL_ARTICLES:
    app.add_page(
        make_article_page(article), 
        route=f"/learn/{article.id}"
    )