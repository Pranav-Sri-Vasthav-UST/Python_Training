import math
distance = int(input("enter the distance: "))
degree = int(input("Enter the degree: "))
tan_value = math.tan(degree)
height_in_feet = tan_value * distance
height_in_meters = height_in_feet * 0.3048
print(f"The building height in meters: {height_in_meters}")
