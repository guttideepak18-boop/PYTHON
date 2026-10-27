
# Multi-Stage Examination Eligibility System

print("===== EXAMINATION ELIGIBILITY SYSTEM =====")

# Get student details
name = input("Enter student name: ")

attendance = float(input("Enter attendance percentage: "))
lab = input("Are all laboratory experiments completed? (yes/no): ").strip().lower()
internal_marks = float(input("Enter internal assessment marks (out of 100): "))
fees = input("Are all fees paid? (yes/no): ").strip().lower()

# Check requirements
unmet = []

if attendance < 75:
    unmet.append("Attendance must be at least 75%.")

if lab != "yes":
    unmet.append("Laboratory work is not completed.")

if internal_marks < 40:
    unmet.append("Internal assessment marks must be at least 40.")

if fees != "yes":
    unmet.append("Fee payment is pending.")

# Display report
print("\n===== ELIGIBILITY REPORT =====")
print("Student Name:", name)

if len(unmet) == 0:
    print("Status: ELIGIBLE")
    print("You are eligible for the final examination.")
else:
    print("Status: NOT ELIGIBLE")
    print("Unmet Requirements:")

    for requirement in unmet:
        print("-", requirement)

print("===== END OF REPORT =====")
