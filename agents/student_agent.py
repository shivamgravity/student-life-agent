from llm.groq_client import ask_llm
from agents.tools_registry import TOOLS


def student_agent(question):

    # Step 1: Ask LLM which tool to use
    tool_prompt = f"""
You are an AI assistant.

User question: {question}

Available tools:
- get_assignments → use when user asks about assignments or deadlines

Respond ONLY with the tool name to use.
If no tool needed, say NONE.
"""

    tool_choice = ask_llm(tool_prompt).strip()

    # Step 2: Execute tool if needed
    tool_result = None

    if tool_choice in TOOLS:
        tool_result = TOOLS[tool_choice]()

    # Step 3: Generate final response
    final_prompt = f"""
User question: {question}

Tool used: {tool_choice}

Tool result:
{tool_result}

Generate a helpful answer.
"""

    return ask_llm(final_prompt)