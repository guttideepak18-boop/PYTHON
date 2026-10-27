
# Student Email and Identifier Validation

print("===== STUDENT VALIDATION SYSTEM =====")

email = input("Enter student email: ").strip()
student_id = input("Enter student registration ID: ").strip()

email_valid = True
id_valid = True

# Email validation
if email == "":
    print("Email Error: Email is missing.")
    email_valid = False

if " " in email:
    print("Email Error: Spaces are not allowed.")
    email_valid = False

if email.count("@") != 1:
    print("Email Error: Must contain exactly one @.")
    email_valid = False
else:
    username, domain = email.split("@")

    if username == "":
        print("Email Error: Username is missing.")
        email_valid = False

    if domain == "":
        print("Email Error: Domain is missing.")
        email_valid = False

    if "." not in domain:
        print("Email Error: Domain must contain a dot.")
        email_valid = False

    if domain.startswith(".") or domain.endswith("."):
        print("Email Error: Invalid dot position.")
        email_valid = False

    if ".." in email:
        print("Email Error: Consecutive dots are not allowed.")
        email_valid = False

    allowed_chars = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789._-@"
    )

    for ch in email:
        if ch not in allowed_chars:
            print("Email Error: Invalid character:", ch)
            email_valid = False
            break

# Registration ID format: CSE followed by 3 digits
if len(student_id) != 6:
    print("ID Error: ID must contain 6 characters.")
    id_valid = False

if not student_id.startswith("CSE"):
    print("ID Error: ID must start with CSE.")
    id_valid = False

if len(student_id) == 6:
    if not student_id[3:].isdigit():
        print("ID Error: Last 3 characters must be digits.")
        id_valid = False

# Display results
print("\n===== VALIDATION RESULTS =====")

if email_valid:
    print("Email: Valid")
else:
    print("Email: Invalid")

if id_valid:
    print("Registration ID: Valid")
else:
    print("Registration ID: Invalid")

if email_valid and id_valid:
    print("Student details are valid.")
else:
    print("Please correct the errors.")

print("===== END OF REPORT =====")


