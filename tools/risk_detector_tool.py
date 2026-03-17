from datetime import datetime

def detect_risks(assignments):
    """
    Detects urgent assignments (due in 1 day or less)
    """

    warnings = []
    today = datetime.now()

    for a in assignments:
        due = datetime.strptime(a["due"], "%Y-%m-%d")
        days_left = (due - today).days

        if days_left <= 1:
            warnings.append(f"{a['title']} is due very soon!")

    return warnings