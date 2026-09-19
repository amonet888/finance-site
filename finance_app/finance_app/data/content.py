from ast import If

from finance_app.data.models import ArticleData

CREDIT_READINESS= ArticleData(
    id="CREDIT READINESS",
    category="Credit",
    title="Before Your First Swipe: Are You Credit-Card Ready?",
    read_time="3 min read",
    author_info="Written by A. Monet",
    intro_text="Getting your first credit card is a big deal. Your name is on the account, you make your own decisions, and you get more independence. But before you apply, think about more than just getting approved. Ask yourself, What is my plan for paying this back? Start by choosing one expense you already budget for, like gas or a phone bill. Set aside that amount from money you have now, instead of relying on extra work, a future refund, or help that might not come.Think of this as practice, not a test of your value. If setting aside the money means you would not have enough for groceries or rent, it is smart to wait.",
    mid_text="Before you apply, write down your answers to three questions: What will I use the card for? How much can I repay without borrowing from somewhere else? When will I check the statement? Next, look at the fees and terms, not just the rewards. A small study by Lim and others found that rewards and loose spending limits can lead young people to overspend. This is a warning, not a prediction about you. (Lim et al., 2014) If you do not have much credit history, a secured card could be an option. It usually needs a deposit and may have fees or high interest rates. (CFPB, How to Rebuild Your Credit) Ask the card company how the deposit works, if they report payments to credit bureaus, and what you need to do to get your deposit back.",
    closing_text="Aim to pay your full statement balance by the due date. If your card has a grace period, paying in full and on time helps you avoid interest. But if you carry a balance, you could lose that benefit. (CFPB, Grace Periods) Your first card does not have to pay for a new lifestyle. It can just cover a small expense you already know how to handle. Make a simple rule for yourself: I will use this card only for ___, set aside the money to pay it back, and check it every ___.” If you are not sure how to fill in the blanks, keep practicing before you apply.",
    head_image_label="readycredit",
    paragraph_photo_label="ready credit-2",
    sources=["Lim et al.: Understanding Young Consumer Perceptions on Credit Card Usage"
             "CFPB: How to Rebuild Your Credit"
             "CFPB: What Is a Grace Period for a Credit Card?"]
    )

INVESTING_101 = ArticleData(
    id="investing-101",
    category="Investing",
    title="Your First Investment Starts With a Goal, Not a Stock",
    read_time="4 min read",
    author_info="Written by A. Monet",
    intro_text="Before you decide what to buy, think about what you need the money for. Saving for an apartment deposit next spring is a different conversation than planning for retirement years from now. The SEC says your time frame and comfort with risk are important when picking investments, and it reminds us that investments can lose value. (Investor.gov, Asset Allocation Guide) Just because you are young does not mean all your money should be invested for the long term.",
    mid_text="Begin by sorting your money into three groups: money for regular bills, money for emergencies, and money you can leave invested. Make sure you do not count the same money in more than one group. For surprise expenses, it is better to have a separate cash reserve instead of relying only on your investments. The CFPB suggests keeping emergency money safe and easy to access, and setting a savings goal that fits your needs. (CFPB, Emergency Fund Guide) Access to an investing app is not the same as preparation. Gupta and Kumar’s review of young adults in Delhi NCR describes a gap between expanding financial access and understanding concepts such as risk and diversification. (Gupta and Kumar, 2026)",
    closing_text="If you are balancing expensive debt, essential expenses, or an unstable paycheck, factor those realities in before deciding how much to invest. Don't force a contribution that immediately sends you back to borrowing. Your next small step. Complete this sentence: “I am considering investing for ___, I expect to need the money around ___, and I can contribute ___ without using bill or emergency money.” “Not yet” is a valid answer while you strengthen your foundation.",
    head_image_label="investor.",
    paragraph_photo_label="investor-2",
    sources=["Gupta and Kumar: Financial Literacy and Investment Behaviour Among Young Adults in Delhi NCR"
             "Investor.gov: Beginners’ Guide to Asset Allocation, Diversification, and Rebalancing"
             "CFPB: An Essential Guide to Building an Emergency Fund"]
)

SPENDING_HABITS= ArticleData(
    id="SPENDING HABITS",
    category="SPENDING",
    title="Pause the Purchase, Not Your Joy",
    read_time="3 min read",
    author_info="Written by A. Monet",
    intro_text="You can enjoy things like clothes, games, travel, beauty products, books, or dinner with friends without seeing every want as a financial problem. The key is to ask if a purchase matches your priorities and budget. For things you don’t need right away, try waiting before you buy. Save the item, close the checkout page, and come back to it later when you’re ready to decide. This is just a suggestion to try out, not a proven rule. Don’t use it for urgent needs like medicine, important travel, or necessary care.",
    mid_text="When you look at the item again, ask yourself: Did I want this before it went on sale? What would I give up to buy it? Would I still choose it without points, discounts, or pressure from others? Lim and colleaguesʼ interviews with young consumers identiﬁed rewards and social desires as relevant to credit-card spending, but the small qualitative sample does not show that everyone responds in the same way. (Lim et al., 2014) Use the questions to notice your own pattern rather than assume you have someone elseʼs. You might also try making optional shopping slightly less automatic. Remove saved checkout details from one store, mute promotional notiﬁcations, or keep a list instead of browsing when tired.",
    closing_text="Chandranʼs Ireland-based research links digital ﬁnancial tools with both constructive and risky ﬁnancial behaviors, including impulsive spending; it does not prove that a particular app feature caused a purchase. (Chandran, 2026) Treat your settings change as something to evaluate, not a guaranteed ﬁx. It helps to plan for social spending, too. You could say, “I can do dinner, but not the weekend trip,” or “I have $35 for going out this week. Want to pick something together?” Yeung’s program focuses on building good financial habits as part of designing your life. (Yeung, 2026) With that in mind, make sure to spend on what truly matters to you, instead of following strict rules that take away your enjoyment. Pause one optional purchase and suggest one aﬀordable social plan. At the end of the week, notice which choice felt more aligned with what you actually wanted.",
    head_image_label="Spending Habits",
    paragraph_photo_label="Spending Habits-2",
    sources=  ['Lim et al.: Understanding Young Consumer Perceptions on Credit Card Usage' ,  'Chandran: Impact of FinTech and Digital Banking Adoption', 'Yeung: Future Ready Young Adults']
)
    
EMERGENCY_FUNDS= ArticleData(
    id="EMERGENCY FUNDS",
    category="RAINY DAYS",
    title="You can start your first rainy day fund with a small amount.",
    read_time="2 min read",
    author_info="Written by A. Monet",
    intro_text="You do not need a large amount to start an emergency fund. The CFPB says it is money set aside for unexpected expenses or emergencies, and even a small fund can give you some peace of mind. (CFPB, Emergency Fund Guide) Think of one situation where having extra money would help. It could be paying for a surprise prescription, urgent travel, a repair, or covering a short break in your income. Pick a first savings goal that feels doable for you, like $100 or $250. These are just examples—what matters is giving yourself some breathing room, not matching someone else’s timeline..",
    mid_text="If you put away $10 each week, you would have $100 after ten weeks, not counting interest or withdrawals. This is just an example of how small steps can add up, but everyone’s situation is different. If saving every week is not possible, try putting aside a small part of any extra money you get, like gifts or tax refunds. The CFPB also recommends using these chances, along with regular savings, to grow your emergency fund. (CFPB, Emergency Fund Guide) Make a simple plan by deciding on your goal, how much you can save, how often you will add to it, and where you will keep the money. The CFPB’s savings worksheet can help you with these steps. (CFPB, Savings Plan)",
    closing_text="If setting up automatic transfers might cause an overdraft, try moving money manually after you pay your main bills. If you do not have anything left, it may help to look for support or adjust your payment plan instead of forcing a transfer. Yeung’s curriculum focuses on building habits and flexible planning. (Yeung, 2026) You can use this idea by telling yourself, “I am practicing a savings routine,” and not letting a missed deposit define you. Pick one expense your emergency fund could cover and set a first goal you can reach. Add what you can, even if your first step is just making a plan..",
    head_image_label="emergency funds",
    paragraph_photo_label="flat tire",
    sources=["Yeung: Future Ready Young Adults", "CFPB: An Essential Guide to Building an Emergency Fund", "CFPB: Savings Plan Worksheet"]
    )

# Easily group them into a registry list for dynamic routing
ALL_ARTICLES = [CREDIT_READINESS, INVESTING_101, SPENDING_HABITS, EMERGENCY_FUNDS]