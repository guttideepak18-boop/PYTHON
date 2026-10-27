
import math

# Store geographical coordinates as tuples (latitude, longitude)
points = [
    (16.5062, 80.6480),
    (16.5193, 80.6305),
    (16.5400, 80.6200),
    (16.5500, 80.6000)
]

distances = []

# Calculate distance between successive points
for i in range(len(points) - 1):
    lat1, lon1 = points[i]
    lat2, lon2 = points[i + 1]

    # Distance formula (Euclidean distance)
    distance = math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

    distances.append(distance)

    print(f"Distance from Point {i+1} to Point {i+2}: {distance:.4f}")

# Identify the longest route segment
longest = max(distances)
index = distances.index(longest)

print("\n===== ROUTE ANALYSIS =====")
print(f"Longest route segment: Point {index+1} to Point {index+2}")
print(f"Longest distance: {longest:.4f} degrees")
