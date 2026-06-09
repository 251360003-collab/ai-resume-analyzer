skills_database = [
    "Python",
    "Java",
    "SQL",
    "Machine Learning",
    "HTML",
    "CSS",
    "JavaScript",
    "Data Analysis"
]

with open("resume.txt", "r", encoding="utf-8") as file:
    resume_text = file.read()

found_skills = []

for skill in skills_database:
    if skill.lower() in resume_text.lower():
        found_skills.append(skill)

score = len(found_skills) * 10

print("=== Resume Analysis Report ===")
print("\nDetected Skills:")
for skill in found_skills:
    print("-", skill)

print("\nResume Score:", score, "/100")

missing_skills = [s for s in skills_database if s not in found_skills]

print("\nRecommended Skills:")
for skill in missing_skills:
    print("-", skill)