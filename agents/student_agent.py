from openclaw import Agent

from tools.classroom_tool import get_assignments
from tools.gmail_tool import scan_emails
from tools.calendar_tool import get_calendar
from tools.study_planner_tool import create_study_plan
from tools.risk_detector_tool import detect_risk

student_agent = Agent(
    name="Self Driving Student Agent",
    description="Autonomously manages a student's academic life",
    tools=[
        get_assignments,
        scan_emails,
        get_calendar,
        create_study_plan,
        detect_risk
    ]
)