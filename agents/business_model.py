"""
=========================================================
Business Model Agent
=========================================================
"""

from utils.llm import llm


def business_model(startup_idea):

    prompt = f"""
    You are an expert Startup Business Consultant.

    Create a Business Model Canvas.

    Startup Idea:

    {startup_idea}

    Include:

    1. Value Proposition

    2. Customer Segments

    3. Revenue Streams

    4. Channels

    5. Customer Relationships

    6. Key Activities

    7. Key Resources

    8. Key Partners

    9. Cost Structure
    """

    response = llm.invoke(prompt)

    return response.content