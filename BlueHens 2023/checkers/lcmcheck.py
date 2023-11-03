import math

for i in range(30, 128):
    for j in range(30, 128):
        if math.lcm(i, j) == 6640:
            print(f"Combination found: i={i}, j={j}")