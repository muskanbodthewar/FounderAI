"""
=========================================================
Competitor Analysis Agent
=========================================================
"""

from utils.llm import llm


def competitor_analysis(startup_idea):

    prompt = f"""
    You are a Startup Competitor Analysis Expert.

    Analyze this startup idea:

    {startup_idea}

    Provide the report in the following format:

    1. Top Competitors

    2. Strengths of Competitors

    3. Weaknesses of Competitors

    4. Market Gap

    5. Competitive Advantage

    6. SWOT Analysis

    7. Recommendation
    """

    response = llm.invoke(prompt)

    return response.content