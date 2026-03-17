from llm.groq_client import ask_llm
from agents.tools_registry import TOOLS

def student_agent(question):

    tool_prompt = f"""
You are an AI assistant.

Your job is to decide which tool to use.

User question: {question}

Available tools:
- get_assignments → for assignments
- detect_risks → for urgent deadlines

Rules:
- Return ONLY one:
- get_assignments
- detect_risks
- NONE
"""

    tool_choice = ask_llm(tool_prompt).strip().lower()

    # Force clean output
    if "get_assignments" in tool_choice:
        tool_choice = "get_assignments"
    else:
        tool_choice = "none"

    tool_result = None

    if tool_choice == "get_assignments":
        tool_result = TOOLS["get_assignments"]()
    elif tool_choice == "detect_risks":
        assignments = TOOLS["get_assignments"]()
        tool_result = TOOLS["detect_risks"](assignments)

    final_prompt = f"""
You are a student assistant.

User question: {question}

Tool used: {tool_choice}

Tool result:
{tool_result}

If tool result exists → use it.
If not → answer normally.

Give a helpful response.
"""

    return ask_llm(final_prompt)