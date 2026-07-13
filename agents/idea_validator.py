"""
Idea Validator Agent
This agent checks whether a startup idea is good or not.
"""

from utils.llm import llm


def validate_idea(startup_idea):
    """
    Analyze a startup idea and return feedback.
    """

    prompt = f"""
    You are an experienced startup mentor.

    Analyze the following startup idea:

    {startup_idea}

    Give your response using the following headings:

    1. Startup Summary
    2. Problem Being Solved
    3. Target Customers
    4. Strengths
    5. Weaknesses
    6. Suggestions for Improvement
    7. Overall Feasibility
    """

    response = llm.invoke(prompt)

    return response.content