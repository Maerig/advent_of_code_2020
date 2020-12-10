from functools import reduce
from typing import Generator

with open("input.txt") as f:
    jolt_input = sorted([
        int(l)
        for l in f
    ])


def part_1(jolts):
    differences = {
        1: 0,
        3: 0
    }
    last_jolt = 0  # Charging outlet
    for jolt in jolts:
        differences[jolt - last_jolt] += 1
        last_jolt = jolt

    differences[3] += 1  # Device adapter

    return differences


diff = part_1(jolt_input)
print(diff[1] * diff[3])


def is_valid(combination):
    last_jolt = None
    for jolt in combination:
        if last_jolt is not None and jolt > last_jolt + 3:
            return False
        last_jolt = jolt
    return True


def possible_combinations(group, i=1) -> Generator[list[int], None, None]:
    if i >= len(group) - 1:
        yield group
        return
    for subgroup in possible_combinations(group, i + 1):
        yield subgroup
    for subgroup in possible_combinations(group[:i] + group[i + 1:], i):
        yield subgroup


def combinations(group):
    return len([
        combination
        for combination in possible_combinations(group)
        if is_valid(combination)
    ])


def part_2(jolts):
    groups = []
    group = [0]  # Charging outlet
    last_jolt = 0
    for jolt in jolts:
        if jolt != last_jolt + 1:
            groups.append(group)
            group = []
        group.append(jolt)
        last_jolt = jolt
    if group:
        groups.append(group)
    groups.append([last_jolt + 3])  # Device adapter

    combinations_per_group = [
        combinations(g)
        for g in groups
    ]
    return reduce(lambda x, y: x * y, combinations_per_group)


print(part_2(jolt_input))
