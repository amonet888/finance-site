from finance_app.data.models import ArticleData

CREDIT_101 = ArticleData(
    id="credit-101",
    category="Credit",
    title="Understanding Your Credit Score",
    read_time="3 min read",
    author_info="Written by Financial Literacy Team",
    intro_text="Your credit score is like a financial GPA...",
    mid_text="Factors that make up your score include payment history...",
    closing_text="Start by checking your score regularly...",
    head_image_label="Credit Score Flower Chart",
    paragraph_photo_label="Credit Utilization Diagram",
    sources=["https://www.consumerfinance.gov"]
)

INVESTING_101 = ArticleData(
    id="investing-101",
    category="Investing",
    title="Compound Interest: Planting Your First Seed",
    read_time="4 min read",
    author_info="Written by Investment Education Team",
    intro_text="Investing isn't just for Wall Street...",
    mid_text="Compound interest occurs when the returns...",
    closing_text="The best time to start investing was yesterday...",
    head_image_label="Growth Compound Graph",
    paragraph_photo_label="Seedling to Tree Visual",
    sources=["https://www.sec.gov/investor"]
)

# Easily group them into a registry list for dynamic routing
ALL_ARTICLES = [CREDIT_101, INVESTING_101]