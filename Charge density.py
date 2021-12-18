import math

q = float(input("Amount of charge q> "))
h = float(input("Distance from the surface of the conductor h> "))
print("A grid of (x,y) over which you would like to calculate the charge density")
x = float(input("x> "))
y = float(input("y> "))

print(f"The numerical value of the charge density as a function of position ({x}, {y}) at q={q} and h={h} is:")
print((1/(2*math.pi)) * (-q * h) / (x**2 + y**2 + h**2) ** (3/2) )
