
# Multi-Stage Scholarship Shortlisting

students = [
    {"name": "Ravi", "marks": 85, "attendance": 90, "income": 150000},
    {"name": "Sita", "marks": 92, "attendance": 95, "income": 100000},
    {"name": "Kiran", "marks": 75, "attendance": 80, "income": 200000},
    {"name": "Priya", "marks": 88, "attendance": 85, "income": 120000},
    {"name": "Arun", "marks": 65, "attendance": 90, "income": 90000}
]

MIN_MARKS = 70
MIN_ATTENDANCE = 75
MAX_INCOME = 180000
QUOTA = 3

eligible = []

print("===== SCHOLARSHIP SHORTLISTING =====")

# Stage 1: Check eligibility
for student in students:
    if (student["marks"] >= MIN_MARKS and
        student["attendance"] >= MIN_ATTENDANCE and
        student["income"] <= MAX_INCOME):

        eligible.append(student)

# Stage 2: Rank candidates by marks
eligible.sort(key=lambda x: x["marks"], reverse=True)

# Stage 3: Select candidates within quota
selected = eligible[:QUOTA]

print("\nEligible Candidates:")
for student in eligible:
    print(student["name"], "- Marks:", student["marks"])

print("\n===== FINAL SELECTED CANDIDATES =====")
for rank, student in enumerate(selected, start=1):
    print(f"Rank {rank}: {student['name']} - Marks: {student['marks']}")

print("\nTotal Eligible Candidates:", len(eligible))
print("Scholarship Quota:", QUOTA)
print("Total Selected Candidates:", len(selected))
print("Not Selected:", len(students) - len(selected))
