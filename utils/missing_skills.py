REQUIRED_SKILLS = [
    "python",
    "sql",
    "machine learning",
    "data science",
    "git",
    "github",
    "pandas",
    "numpy",
    "html",
    "css"
]

def find_missing_skills(detected_skills):
    missing = []

    for skill in REQUIRED_SKILLS:
        if skill not in detected_skills:
            missing.append(skill)

    return missing