import re
from collections import defaultdict

BITMASK_REGEX = re.compile(r"^mask = ([X01]+)$")
MEMORY_REGEX = re.compile(r"^mem\[(\d+)\] = (\d+)$")


def apply_bitmask_v1(n, bitmask):
    zeros = int(bitmask.replace("X", "1"), 2)
    ones = int(bitmask.replace("X", "0"), 2)
    return n & zeros | ones


def run_program(program, write_func):
    mask = None
    memory = defaultdict(int)

    for line in program:
        match = BITMASK_REGEX.match(line)
        if match:
            mask = match.group(1)
            continue

        match = MEMORY_REGEX.match(line)
        if match:
            idx, val = match.groups()
            memory = write_func(mask, memory, idx, val)
            continue

        raise ValueError(line)

    return sum(memory.values())


def write_func_p1(mask, memory, idx, val):
    memory[int(idx)] = apply_bitmask_v1(int(val), mask)
    return memory


def floating_variations(bitmask):
    variation_stack = [bitmask]
    while variation_stack:
        variation = variation_stack.pop()
        try:
            x_idx = variation.index("X")
        except ValueError:
            # No more X
            yield variation
            continue

        variation_stack.append(variation[:x_idx] + "0" + variation[x_idx + 1:])
        variation_stack.append(variation[:x_idx] + "1" + variation[x_idx + 1:])


def apply_bitmask_v2(n, bitmask):
    ones = int(bitmask.replace("X", "0"), 2)
    mask_applied = n | ones
    floating = "".join(
        "X" if m == "X" else c
        for c, m in zip(format(mask_applied, "036b"), bitmask)
    )
    for variation in floating_variations(floating):
        yield int(variation)


def write_func_p2(mask, memory, idx, val):
    for address in apply_bitmask_v2(int(idx), mask):
        memory[address] = int(val)
    return memory


with open("input.txt") as f:
    raw_program = [
        line.strip()
        for line in f
    ]


print(run_program(raw_program, write_func_p1))
print(run_program(raw_program, write_func_p2))
