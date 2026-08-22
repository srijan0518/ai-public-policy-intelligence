def calculate_importance(analysis):
    score = 15
    reasons = []

    category = analysis["category"]
    entities = analysis["entities"]

    if category != "General Policy":
        score += 10
        reasons.append(f"Policy domain identified as {category}.")

    orgs = len(entities["organizations"])
    locations = len(entities["locations"])
    dates = len(entities["dates"])
    money = len(entities["money"])

    if orgs:
        points = min(orgs * 4, 16)
        score += points
        reasons.append(f"{orgs} organization references detected (+{points}).")

    if locations:
        points = min(locations * 3, 12)
        score += points
        reasons.append(f"{locations} geographic references detected (+{points}).")

    if dates:
        points = min(dates * 3, 12)
        score += points
        reasons.append(f"{dates} date/time references detected (+{points}).")

    if money:
        points = min(money * 5, 15)
        score += points
        reasons.append(f"{money} financial references detected (+{points}).")

    if analysis["word_count"] >= 500:
        score += 10
        reasons.append("Substantial source content is available for analysis (+10).")

    if analysis["category_score"] >= 0.75:
        score += 10
        reasons.append("Policy-domain classification has high confidence (+10).")

    score = min(score, 100)

    level = (
        "Critical" if score >= 85
        else "High" if score >= 70
        else "Medium" if score >= 45
        else "Low"
    )

    return {"score": score, "level": level, "reasons": reasons}
