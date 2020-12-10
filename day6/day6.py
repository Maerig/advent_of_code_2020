from functools import reduce

groups: list[list[set]] = []
group: list[set] = []
with open("input.txt") as f:
    for l in f:
        if l == "\n":
            groups.append(group)
            group = []
        else:
            group.append(set(l.strip()))
if group:
    groups.append(group)

print(sum(len(reduce(lambda a,b: a | b, g)) for g in groups))
print(sum(len(reduce(lambda a,b: a & b, g)) for g in groups))
