"""
=========================================================
Roadmap Agent
=========================================================
"""

from utils.llm import llm


def roadmap(startup_idea):

    prompt = f"""
    You are a Startup Mentor.

    Startup Idea:

    {startup_idea}

    Create a 12-month roadmap.

    Divide into:

    Month 1-2

    Month 3-4

    Month 5-6

    Month 7-8

    Month 9-10

    Month 11-12

    Final Goal
    """

    response = llm.invoke(prompt)

    return response.content