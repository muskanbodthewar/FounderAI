"""
=========================================================
Market Research Agent

This agent performs market research for a startup idea.
=========================================================
"""

from utils.llm import llm


def market_research(startup_idea):
    """
    Perform market research for the startup idea.
    """

    prompt = f"""
    You are a professional Market Research Analyst.

    Analyze the following startup idea.

    Startup Idea:
    {startup_idea}

    Give your response using these headings:

    1. Industry Overview

    2. Target Market

    3. Competitor Analysis

    4. Market Opportunities

    5. Market Risks

    6. Future Trends

    7. Final Recommendation
    """

    response = llm.invoke(prompt)

    return response.content