"""
=========================================================
Startup Score Agent

Purpose:
---------
This AI agent evaluates a startup idea and gives
a numerical score across multiple business factors.
=========================================================
"""

from utils.llm import llm


def startup_score(startup_idea):
    """
    Evaluate startup idea and return startup score.
    """

    prompt = f"""
You are a startup evaluator.

Analyze the following startup idea.

Startup Idea:
{startup_idea}

Evaluate it using ONLY the following format.

Overall Startup Score: __/100

Innovation: __/10

Market Demand: __/10

Revenue Potential: __/10

Scalability: __/10

Competition Level:
(Low / Medium / High)

Investment Risk:
(Low / Medium / High)

Success Probability:
__%

Finally explain in 5-6 lines why you gave this score.
"""

    response = llm.invoke(prompt)

    return response.content