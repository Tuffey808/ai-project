SKILLS = {"python", "java", "sql", "machine learning", "nlp", "pandas"}

def extract_skills(text):
    text = text.lower()
    found_skills = set()
    for skill in SKILLS:
        if skill in text:
            found_skills.add(skill)
    return list(found_skills)
