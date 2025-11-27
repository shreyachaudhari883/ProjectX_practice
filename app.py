# Addition
sum_result = 10 + 5
print(f"10 + 5 = {sum_result}") # Output: 15

# Subtraction
diff_result = 20 - 7
print(f"20 - 7 = {diff_result}") # Output: 13

# Multiplication
prod_result = 6 * 4
print(f"6 * 4 = {prod_result}") # Output: 24

# Division (results in a float)
div_result = 100 / 8
print(f"100 / 8 = {div_result}") # Output: 12.5

# Integer Division (discards the fractional part)
int_div_result = 100 // 8
print(f"100 // 8 = {int_div_result}") # Output: 12

# Modulo (returns the remainder of the division)
remainder = 10 % 3
print(f"10 % 3 = {remainder}") # Output: 1

# Exponentiation (raising a number to a power)
#power_result = 2 ** 5
#print(f"2 ** 5 = {power_result}") # Output: 32
====================================================
import math

# Convert 45 degrees to radians
angle_degrees = 45
angle_radians = math.radians(angle_degrees)
print(f"45 degrees in radians: {angle_radians}")

# Calculate Sine (sin)
sin_value = math.sin(angle_radians)
print(f"Sin(45°) = {sin_value}")

# Calculate Cosine (cos)
cos_value = math.cos(angle_radians)
print(f"Cos(45°) = {cos_value}")

# Calculate Tangent (tan)
tan_value = math.tan(angle_radians)
print(f"Tan(45°) = {tan_value}")

# Inverse Sine (arcsin) - returns angle in radians
arcsin_value = math.asin(0.5)
print(f"Angle whose sin is 0.5 (in radians): {arcsin_value}")
print(f"Angle in degrees: {math.degrees(arcsin_value)}") # Convert back to degrees
