
# Campus Event Financial Planning

print("=== CAMPUS EVENT FINANCIAL PLANNING ===")

# Input details
participants = int(input("Enter expected participants: "))
registration_fee = float(input("Enter registration fee per participant: "))

venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
catering = float(input("Enter catering cost per participant: Rs. "))
transport = float(input("Enter transport cost per participant: Rs. "))
certificate = float(input("Enter certificate cost per participant: Rs. "))

sponsorship = float(input("Enter sponsorship amount: Rs. "))

# Calculate costs
fixed_cost = venue + equipment
variable_cost = catering + transport + certificate

total_variable_cost = participants * variable_cost
total_cost = fixed_cost + total_variable_cost

# Calculate income
registration_income = participants * registration_fee
total_income = registration_income + sponsorship

# Calculate sponsorship shortfall
shortfall = total_cost - total_income

# Calculate participant contribution needed
if participants > 0:
    contribution = total_cost / participants
else:
    contribution = 0

# Calculate minimum registrations to break even
net_fee = registration_fee - variable_cost

if net_fee > 0:
    if fixed_cost > sponsorship:
        minimum_participants = (
            (fixed_cost - sponsorship) / net_fee
        )
        minimum_participants = int(minimum_participants)

        if minimum_participants * net_fee < fixed_cost - sponsorship:
            minimum_participants += 1
    else:
        minimum_participants = 0
else:
    minimum_participants = -1

# Display report
print("\n===== EVENT FINANCIAL REPORT =====")
print("Fixed costs: Rs.", round(fixed_cost, 2))
print("Variable cost per participant: Rs.", round(variable_cost, 2))
print("Total event cost: Rs.", round(total_cost, 2))
print("Registration income: Rs.", round(registration_income, 2))
print("Sponsorship: Rs.", round(sponsorship, 2))
print("Total income: Rs.", round(total_income, 2))
print("Contribution needed per participant: Rs.",
      round(contribution, 2))

if shortfall > 0:
    print("Financial shortfall: Rs.", round(shortfall, 2))
elif shortfall < 0:
    print("Expected surplus: Rs.", round(-shortfall, 2))
else:
    print("Event breaks even!")

if minimum_participants == -1:
    print("Break-even is not possible with this registration fee.")
elif minimum_participants == 0:
    print("Sponsorship covers all fixed costs.")
else:
    print("Minimum registrations to break even:",
          minimum_participants)

print("\n===== END OF REPORT =====")
