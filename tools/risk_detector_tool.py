def detect_risk(assignments):

    warnings = []

    for a in assignments:
        if a["due"] == "tomorrow":
            warnings.append(
                f"{a['title']} is due tomorrow."
            )

    return warnings