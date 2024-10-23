import math

x = -4.0
h = 0.2
conec = 4.2

while x <= conec:
    calculate = math.cos(x) / (2+x)
    print(f"x = {x:.1f}, y = {calculate:.5f}")
    x += h
