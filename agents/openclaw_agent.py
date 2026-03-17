from openclaw import Agent # type: ignore

from tools.classroom_tool import get_assignments
from tools.risk_detector_tool import detect_risks


openclaw_agent = Agent(
    name="Student Assistant Agent",
    description="Manages student assignments and detects risks",
    tools=[
        get_assignments,
        detect_risks
    ]
)