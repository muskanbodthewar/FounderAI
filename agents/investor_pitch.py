"""
=========================================================
Investor Pitch Agent
=========================================================
"""

from utils.llm import llm


def investor_pitch(startup_idea):

    prompt = f"""
    You are a Startup Investor.

    Prepare an investor pitch.

    Startup Idea:

    {startup_idea}

    Include:

    1. Problem

    2. Solution

    3. Market Opportunity

    4. Business Model

    5. Revenue Model

    6. Competitive Advantage

    7. Funding Ask

    8. Vision
    """

    response = llm.invoke(prompt)

    return response.content