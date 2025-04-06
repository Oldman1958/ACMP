from math import pi
s, r_1 = map(float, input().split())
r_2 = round(((pi*(r_1**2) - s) / pi)**0.5, 3)
print(r_2)
"""
s = pi*(r_1**2) - pi*(r_2**2)
s - pi*(r_1**2) = -pi*(r_2**2)
pi*(r_2**2) = pi*(r_1**2) - s
r_2**2 = (pi*(r_1**2) - s) / pi
r_2 = round(((pi*(r_1**2) - s) / pi)**0.5, 3)
"""
