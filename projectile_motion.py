import math

# Input
velocity = float(input("Enter initial velocity (m/s): "))
angle = float(input("Enter angle of projection (degrees): "))

# Convert angle to radians
angle_rad = math.radians(angle)

# Calculations
g = 9.81

time_of_flight = (2 * velocity * math.sin(angle_rad)) / g

maximum_height = (velocity**2 * math.sin(angle_rad)**2) / (2 * g)

range_of_projectile = (velocity**2 * math.sin(2 * angle_rad)) / g

# Output
print("Time of flight:", round(time_of_flight, 2), "seconds")
print("Maximum height:", round(maximum_height, 2), "meters")
print("Range:", round(range_of_projectile, 2), "meters")
