from llm.groq_client import ask_llm
from agents.tools_registry import TOOLS
from agents.openclaw_agent import openclaw_agent

def student_agent(question):

    tool_prompt = f"""
You are an AI assistant that selects tools.

User question: {question}

Available tools:
- get_assignments → for assignments, deadlines, tasks
- detect_risks → for urgency, urgent work, deadlines soon

Rules:
- If question contains words like "urgent", "soon", "deadline" → use detect_risks
- If question asks about assignments → use get_assignments
- Otherwise → NONE

Respond with ONLY:
get_assignments
detect_risks
NONE
"""

    tool_choice = ask_llm(tool_prompt).strip().lower()

    # debugging
    print(f"Tool chosen: {tool_choice}")

    # Priority-based decision
    if "urgent" in question.lower() or "soon" in question.lower() or "deadline" in question.lower():
        tool_choice = "detect_risks"
    elif "get_assignments" in tool_choice:
        tool_choice = "get_assignments"
    elif "detect_risks" in tool_choice:
        tool_choice = "detect_risks"
    else:
        tool_choice = "none"

    tool_result = None

    if tool_choice == "get_assignments":
        tool_result = openclaw_agent.run("Get assignments")
    elif tool_choice == "detect_risks":
        tool_result = openclaw_agent.run("Check urgent assignments")

    final_prompt = f"""
You are a student assistant.

User question: {question}

Tool used: {tool_choice}

Tool result:
{tool_result}

IMPORTANT:
- If tool_result contains warnings → show them clearly
- DO NOT say "nothing urgent" if warnings exist
- DO NOT hallucinate

Answer clearly.
"""

    return ask_llm(final_prompt)