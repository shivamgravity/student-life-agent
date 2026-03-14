def generate_study_plan(assignments):

    plan = []

    for a in assignments:
        plan.append(
            f"Study for {a['title']} before {a['due']}"
        )

    return plan