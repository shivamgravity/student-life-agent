from openclaw import CMDOPClient # type: ignore

client = CMDOPClient()

def openclaw_execute(task: str):
    """
    Executes a task using OpenClaw
    """

    try:
        result = client.run(task)
        return result
    except Exception as e:
        return f"OpenClaw error: {str(e)}"