def get_suggestions(skills):
    suggestions = []

    if "github" not in skills:
        suggestions.append("Add your GitHub profile.")

    if "git" not in skills:
        suggestions.append("Learn and mention Git.")

    if "sql" not in skills:
        suggestions.append("Add SQL skills if you know them.")

    if "python" not in skills:
        suggestions.append("Add Python projects and skills.")

    if len(skills) < 5:
        suggestions.append("Include more technical skills and projects.")

    return suggestions