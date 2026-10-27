
# Campus Transport Allocation

routes = {
    "Route 1": {"passengers": 120, "capacity": 40},
    "Route 2": {"passengers": 95, "capacity": 30},
    "Route 3": {"passengers": 75, "capacity": 25}
}

total_buses = 0
total_unserved = 0

print("===== CAMPUS TRANSPORT ALLOCATION =====")

for route, details in routes.items():
    passengers = details["passengers"]
    capacity = details["capacity"]

    # Calculate buses required
    buses = (passengers + capacity - 1) // capacity

    # Calculate unserved passengers
    served_passengers = min(passengers, buses * capacity)
    unserved = passengers - served_passengers

    total_buses += buses
    total_unserved += unserved

    print(f"\n{route}")
    print(f"Passenger Demand: {passengers}")
    print(f"Bus Capacity: {capacity}")
    print(f"Buses Needed: {buses}")
    print(f"Unserved Passengers: {unserved}")

print("\n===== FINAL REPORT =====")
print("Total Buses Needed:", total_buses)
print("Total Unserved Passengers:", total_unserved)
