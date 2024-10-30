import math

x = -4.0
h = 0.2
conec = 4.2

while x <= conec:
    calculate = math.cos(x) / (2+x)
    x += h
    print((f"x = {(x)}, y = {(calculate)}"))