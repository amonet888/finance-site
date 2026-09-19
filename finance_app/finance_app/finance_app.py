import reflex as rx
from finance_app.data.content import ALL_ARTICLES
from finance_app.pages.article_player import article_player
from finance_app.pages.test_index import test_index_page

app = rx.App()

# Registers the testing hub as the default homepage
app.add_page(test_index_page, route="/")

# Helper function to create a page renderer for a specific article
def make_article_page(selected_article):
    return lambda: article_player(selected_article)

# Register routes cleanly without lambda parameter warnings
for article in ALL_ARTICLES:
    app.add_page(
        make_article_page(article), 
        route=f"/learn/{article.id}"
    )