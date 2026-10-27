
# University Academic Progression Audit

students = [
    {
        "id": 101,
        "name": "Ravi",
        "semester_marks": [75, 80, 65, 90],
        "attendance": 85,
        "prerequisites": True
    },
    {
        "id": 102,
        "name": "Sita",
        "semester_marks": [80, 35, 70, 60],
        "attendance": 90,
        "prerequisites": True
    },
    {
        "id": 103,
        "name": "Kiran",
        "semester_marks": [65, 70, 55, 80],
        "attendance": 68,
        "prerequisites": False
    }
]

PASS_MARK = 40
MIN_ATTENDANCE = 75

print("===== UNIVERSITY ACADEMIC PROGRESSION AUDIT =====")

for student in students:
    print(f"\nStudent ID: {student['id']}")
    print(f"Student Name: {student['name']}")

    marks = student["semester_marks"]
    attendance = student["attendance"]
    prerequisites = student["prerequisites"]

    passed = 0
    outstanding = []

    # Check subject marks
    for i, mark in enumerate(marks, start=1):
        if mark >= PASS_MARK:
            passed += 1
        else:
            outstanding.append(f"Subject {i} - Failed")

    # Check attendance
    if attendance < MIN_ATTENDANCE:
        outstanding.append("Attendance requirement not met")

    # Check prerequisites
    if not prerequisites:
        outstanding.append("Prerequisite completion pending")

    average = sum(marks) / len(marks)

    print("Semester Marks:", marks)
    print(f"Average Marks: {average:.2f}")
    print(f"Subjects Passed: {passed}/{len(marks)}")
    print(f"Attendance: {attendance}%")
    print("Prerequisites Completed:", prerequisites)

    # Determine progression eligibility
    if len(outstanding) == 0:
        print("Progression Status: ELIGIBLE")
        print("Outstanding Requirements: None")
    else:
        print("Progression Status: NOT ELIGIBLE")
        print("Outstanding Requirements:")
        for requirement in outstanding:
            print("-", requirement)

print("\n===== AUDIT COMPLETED =====")
