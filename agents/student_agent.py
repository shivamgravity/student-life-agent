from tools.classroom_tool import get_assignments
from tools.study_planner_tool import generate_study_plan
from llm.groq_client import ask_llm


def student_agent(question):

    assignments = get_assignments()
    plan = generate_study_plan(assignments)

    prompt = f"""
You are a helpful student assistant.

User Question:
{question}

Assignments:
{assignments}

Study Plan:
{plan}

Answer clearly and helpfully.
"""

    return ask_llm(prompt)