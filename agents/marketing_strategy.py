"""
=========================================================
Marketing Strategy Agent
=========================================================
"""

from utils.llm import llm


def marketing_strategy(startup_idea):

    prompt = f"""
    You are a Digital Marketing Expert.

    Startup Idea:

    {startup_idea}

    Create a complete marketing strategy.

    Include:

    1. Branding

    2. Social Media Plan

    3. SEO Strategy

    4. Customer Acquisition

    5. Paid Advertising

    6. Growth Strategy

    7. Launch Plan
    """

    response = llm.invoke(prompt)

    return response.content