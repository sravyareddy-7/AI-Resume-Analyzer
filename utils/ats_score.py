def calculate_ats_score(skills):
    total_skills = 10

    score = min((len(skills) / total_skills) * 100, 100)

    return round(score, 2)