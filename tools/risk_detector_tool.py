from datetime import datetime

def detect_risks(assignments):

    warnings = []

    today = datetime.now()

    for a in assignments:

        due_date = datetime.strptime(a["due"], "%Y-%m-%d")

        days_left = (due_date - today).days

        if days_left <= 1:
            warnings.append(
                f"⚠️ {a['title']} is due very soon."
            )

    return warnings