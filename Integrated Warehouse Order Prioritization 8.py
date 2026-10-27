
# Integrated Warehouse Order Prioritization

orders = [
    {"id": 101, "product": "Laptop", "demand": 50,
     "stock": 30, "quantity": 20, "priority": "High"},

    {"id": 102, "product": "Mouse", "demand": 40,
     "stock": 50, "quantity": 25, "priority": "Low"},

    {"id": 103, "product": "Keyboard", "demand": 30,
     "stock": 20, "quantity": 15, "priority": "Medium"},

    {"id": 104, "product": "Monitor", "demand": 25,
     "stock": 10, "quantity": 20, "priority": "High"}
]

# Process high-priority orders first
priority_order = {"High": 1, "Medium": 2, "Low": 3}
orders.sort(key=lambda x: priority_order[x["priority"]])

print("===== WAREHOUSE ORDER PRIORITIZATION =====")

for order in orders:
    demand = order["demand"]
    stock = order["stock"]
    quantity = order["quantity"]

    # Calculate available stock for the order
    available = min(stock, demand, quantity)
    outstanding = quantity - available

    # Check fulfilment feasibility
    if outstanding == 0:
        status = "Fully Fulfilled"
    elif available > 0:
        status = "Partially Fulfilled"
    else:
        status = "Not Fulfilled"

    print(f"\nOrder ID: {order['id']}")
    print(f"Product: {order['product']}")
    print(f"Priority: {order['priority']}")
    print(f"Demand: {demand}")
    print(f"Stock: {stock}")
    print(f"Order Quantity: {quantity}")
    print(f"Fulfilled Quantity: {available}")
    print(f"Outstanding Quantity: {outstanding}")
    print(f"Status: {status}")
