import math

x = -4.0
h = 0.2
conec = 4.0

while x <= conec:
    calculate = math.cos(x) / (2+x)
    x += h
    print((f"x = {(round(x,2))}, y = {(calculate)}"))
