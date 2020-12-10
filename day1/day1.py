from itertools import combinations

with open("input.txt") as f:
    entries = [int(n.strip()) for n in f.readlines()]

for x, y in combinations(entries, 2):
    if x + y == 2020:
        print(f"{x} * {y} = {x * y}")
        break

for x, y, z in combinations(entries, 3):
    if x + y + z == 2020:
        print(f"{x} * {y} * {z} = {x * y * z}")
        break
