
# University Admission Decision Engine

applicants = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print("\nApplicant", i + 1)

    name = input("Enter applicant name: ")
    maths = float(input("Enter Mathematics marks: "))
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))
    aggregate = float(input("Enter aggregate percentage: "))

    applicants.append(
        (name, maths, physics, chemistry, aggregate)
    )

# Course eligibility criteria
maths_minimum = 50
physics_minimum = 50
chemistry_minimum = 50
aggregate_minimum = 60

eligible = []

# Check eligibility
for applicant in applicants:
    name, maths, physics, chemistry, aggregate = applicant

    if (maths >= maths_minimum
            and physics >= physics_minimum
            and chemistry >= chemistry_minimum
            and aggregate >= aggregate_minimum):

        eligible.append(applicant)

# Rank eligible applicants
# Higher aggregate first; higher Mathematics marks break ties
for i in range(len(eligible)):
    for j in range(i + 1, len(eligible)):
        if (eligible[j][4] > eligible[i][4]
                or (eligible[j][4] == eligible[i][4]
                    and eligible[j][1] > eligible[i][1])):

            eligible[i], eligible[j] = eligible[j], eligible[i]

# Display ranked list
print("\n===== UNIVERSITY ADMISSION RESULTS =====")

if len(eligible) == 0:
    print("No eligible applicants found.")
else:
    print("Rank | Name | Maths | Physics | Chemistry | Aggregate")

    for i in range(len(eligible)):
        name, maths, physics, chemistry, aggregate = eligible[i]

        print(i + 1, "|", name, "|", maths, "|",
              physics, "|", chemistry, "|", aggregate)

print("\nTotal applicants:", n)
print("Eligible applicants:", len(eligible))
print("Not eligible applicants:", n - len(eligible))

print("\n===== END OF REPORT =====")
