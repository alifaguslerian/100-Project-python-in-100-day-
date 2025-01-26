student_scores = input("Enter student scores separated by commas:")
scores = [int(score) for score in student_scores.split(",")]

grades = [
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "E"
    for score in scores
]

passing_students = [score for score in scores if score >= 60]
falling__students = [score for score in scores if score < 60]

print("\n--- Student Grades ---")
for i, (score, grade) in enumerate(zip(scores, grades), start=1):
    print(f"Student {i}: Score: {score}, Grade: {grade}")

print("\n--- Passing and falling Students ---")
print("passing students:", passing_students)
print("falling students:", falling__students)

