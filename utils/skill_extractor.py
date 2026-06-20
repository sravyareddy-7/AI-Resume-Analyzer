SKILLS = [
    "python", "java", "c", "c++", "javascript",
    "html", "css", "react", "node.js", "mongodb",
    "sql", "mysql", "machine learning",
    "data science", "pandas", "numpy",
    "deep learning", "git", "github"
]

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))