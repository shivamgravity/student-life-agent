import schedule
import time

from agents.student_agent import student_agent

def run_daily_check():

    result = student_agent.run(
        "Check assignments and create today's study plan"
    )

    print(result)

schedule.every().day.at("08:00").do(run_daily_check)

while True:
    schedule.run_pending()
    time.sleep(60)