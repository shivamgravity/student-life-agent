from llm.groq_client import ask_llm
from agents.tools_registry import TOOLS
from agents.openclaw_wrapper import openclaw_execute


def student_agent(question):

    # 🔹 Step 1: Tool selection prompt
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

    # 🔹 Debugging
    print(f"Tool chosen (LLM): {tool_choice}")

    # 🔥 Step 2: Rule-based override (deterministic)
    if "urgent" in question.lower() or "soon" in question.lower() or "deadline" in question.lower():
        tool_choice = "detect_risks"
    elif "get_assignments" in tool_choice:
        tool_choice = "get_assignments"
    elif "detect_risks" in tool_choice:
        tool_choice = "detect_risks"
    else:
        tool_choice = "none"

    print(f"Tool chosen (final): {tool_choice}")

    # 🔹 Step 3: Execute tool
    tool_result = None

    if tool_choice == "get_assignments":
        openclaw_execute("Fetching assignments using OpenClaw")
        tool_result = TOOLS["get_assignments"]()

    elif tool_choice == "detect_risks":
        openclaw_execute("Checking urgent assignments using OpenClaw")

        assignments = TOOLS["get_assignments"]()
        tool_result = TOOLS["detect_risks"](assignments)

    # 🔹 Step 4: Final response generation
    final_prompt = f"""
You are a student assistant.

User question: {question}

Tool used: {tool_choice}

Tool result:
{tool_result}

IMPORTANT:
- If tool_result contains warnings → show them clearly
- If tool_result is empty → say nothing urgent
- DO NOT hallucinate
- DO NOT invent assignments

Answer clearly.
"""

    return ask_llm(final_prompt)