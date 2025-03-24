import math

# Function to calculate the distance between two points
def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Function to check if the points form a right-angle triangle
def is_right_angle_triangle(a, b, c):
    side1 = distance(a, b) ** 2
    side2 = distance(b, c) ** 2
    side3 = distance(a, c) ** 2
    sides = sorted([side1, side2, side3])
    return math.isclose(sides[0] + sides[1], sides[2])

# Function to check if the points form an isosceles triangle
def is_isosceles_triangle(a, b, c):
    side1 = distance(a, b)
    side2 = distance(b, c)
    side3 = distance(a, c)
    return math.isclose(side1, side2) or math.isclose(side2, side3) or math.isclose(side1, side3)

# List of all test cases with corresponding names
test_cases = [
    {"name": "Right-Angle Isosceles Triangle", "points": [(0, 0), (1, 0), (0, 1)]},
    {"name": "Right-Angle Triangle (Not Isosceles)", "points": [(0, 0), (3, 0), (0, 4)]},
    {"name": "Isosceles Triangle (Not Right-Angle)", "points": [(0, 0), (2, 4), (4, 0)]},
    {"name": "Neither Right-Angle Nor Isosceles Triangle", "points": [(0, 0), (1, 2), (3, 4)]}
]

# Loop through all the test cases
for idx, case in enumerate(test_cases, start=1):
    point1, point2, point3 = case["points"]

    # Calculate the distances between the points
    dist1 = distance(point1, point2)
    dist2 = distance(point2, point3)
    dist3 = distance(point1, point3)

    # Check all conditions in a single if-else block
    print(f"\nTest Case {idx}: {case['name']}")
    
    if is_right_angle_triangle(point1, point2, point3) and is_isosceles_triangle(point1, point2, point3):
        print("The points form a right-angle isosceles triangle.")
    elif is_right_angle_triangle(point1, point2, point3):
        print("The points form a right-angle triangle.")
    elif is_isosceles_triangle(point1, point2, point3):
        print("The points form an isosceles triangle.")
    else:
        print("The points do not form a right-angle, isosceles, or right-angle isosceles triangle.")

    # Print the distances for reference
    print(f"Distance between Point1 and Point2: {dist1:.2f}")
    print(f"Distance between Point2 and Point3: {dist2:.2f}")
    print(f"Distance between Point1 and Point3: {dist3:.2f}")