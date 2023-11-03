import math

for i in range(30, 128):
    for j in range(30, 128):
        if i ** 2 - j ** 2 == 952:
            print(f"Combination found: i={i}, j={j}")