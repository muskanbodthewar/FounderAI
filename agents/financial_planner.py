"""
=========================================================
Financial Planning Agent
=========================================================
"""

from utils.llm import llm


def financial_planner(startup_idea):

    prompt = f"""
    You are a Startup Financial Advisor.

    Startup Idea:

    {startup_idea}

    Create a financial plan.

    Include:

    1. Estimated Initial Investment

    2. Monthly Expenses

    3. Revenue Streams

    4. Pricing Strategy

    5. Break-even Analysis

    6. Funding Requirement

    7. Profit Potential
    """

    response = llm.invoke(prompt)

    return response.content