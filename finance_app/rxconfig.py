import reflex as rx

config = rx.Config(
    app_name="finance_app",
    stylesheets=["styles.css"],
    backend_port=8000,
    frontend_port=3000,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(),
    ]
)