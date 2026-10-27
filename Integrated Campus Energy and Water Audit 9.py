
# Integrated Campus Energy and Water Audit

buildings = {
    "CSE Block": {
        "energy": [500, 600, 750],
        "water": [1000, 1100, 1400]
    },
    "Library": {
        "energy": [300, 350, 400],
        "water": [800, 850, 900]
    },
    "Hostel": {
        "energy": [700, 750, 900],
        "water": [1500, 1700, 2000]
    },
    "Admin Block": {
        "energy": [250, 280, 300],
        "water": [500, 550, 600]
    }
}

ENERGY_RATE = 8       # Cost per energy unit
WATER_RATE = 0.05     # Cost per water unit
ENERGY_LIMIT = 650    # Excessive daily energy consumption
WATER_LIMIT = 1600    # Excessive daily water consumption

results = []

print("===== CAMPUS ENERGY AND WATER AUDIT =====")

for building, data in buildings.items():
    energy = data["energy"]
    water = data["water"]

    total_energy = sum(energy)
    total_water = sum(water)

    energy_cost = total_energy * ENERGY_RATE
    water_cost = total_water * WATER_RATE
    total_cost = energy_cost + water_cost

    # Percentage change from first day to last day
    energy_change = ((energy[-1] - energy[0]) / energy[0]) * 100
    water_change = ((water[-1] - water[0]) / water[0]) * 100

    # Identify excessive consumption
    high_energy = any(x > ENERGY_LIMIT for x in energy)
    high_water = any(x > WATER_LIMIT for x in water)

    # Scoring method: 1 point for each excessive category
    score = int(high_energy) + int(high_water)

    results.append({
        "building": building,
        "energy": total_energy,
        "water": total_water,
        "cost": total_cost,
        "energy_change": energy_change,
        "water_change": water_change,
        "high_energy": high_energy,
        "high_water": high_water,
        "score": score
    })

    print(f"\nBuilding: {building}")
    print(f"Total Energy: {total_energy} units")
    print(f"Total Water: {total_water} units")
    print(f"Energy Cost: Rs. {energy_cost:.2f}")
    print(f"Water Cost: Rs. {water_cost:.2f}")
    print(f"Total Cost: Rs. {total_cost:.2f}")
    print(f"Energy Change: {energy_change:.2f}%")
    print(f"Water Change: {water_change:.2f}%")
    print("Excessive Energy:", "Yes" if high_energy else "No")
    print("Excessive Water:", "Yes" if high_water else "No")
    print("Audit Score:", score)

# Rank buildings by score, then total cost
results.sort(key=lambda x: (x["score"], x["cost"]), reverse=True)

print("\n===== BUILDING RANKING =====")
for rank, result in enumerate(results, start=1):
    print(
        f"Rank {rank}: {result['building']} | "
        f"Score: {result['score']} | "
        f"Total Cost: Rs. {result['cost']:.2f}"
    )
