from openclaw import Agent

from tools.classroom_tool import get_assignments
from tools.gmail_tool import scan_emails
from tools.calendar_tool import get_calendar_events
from tools.study_planner_tool import generate_study_plan
from tools.risk_detector_tool import detect_risks

student_agent = Agent(
    name="Student Life Agent",
    description="Autonomous agent that manages student assignments and schedules.",
    tools=[
        get_assignments,
        scan_emails,
        get_calendar_events,
        generate_study_plan,
        detect_risks
    ]
)