import schedule # type: ignore
import time
import os
import sys

target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'agents'))
sys.path.append(target_dir)
target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'telegram'))
sys.path.append(target_dir)

from agents.student_agent import student_agent
from telegram.send_message import send_telegram_message


def run_daily_check():

    print("Running daily student check...")

    response = student_agent("Do I have anything urgent today?")

    message = f"""
📚 Daily Academic Update

{response}
"""

    send_telegram_message(message)

    print("Message sent!")


# Run every day at 8 AM
# schedule.every().day.at("08:00").do(run_daily_check)
schedule.every(1).minutes.do(run_daily_check)

while True:
    schedule.run_pending()
    time.sleep(60)