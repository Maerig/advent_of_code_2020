from itertools import combinations


PREAMBLE_SIZE = 25


def is_valid(i, numbers):
    return any(
        x + y == numbers[i]
        for x, y in combinations(numbers[i - PREAMBLE_SIZE : i], 2)
    )


def get_first_invalid(numbers):
    i = PREAMBLE_SIZE
    while True:
        if not is_valid(i, numbers):
            return numbers[i]
        i += 1


def get_contiguous_range(numbers, target):
    for range_length in range(2, len(numbers)):
        for i in range(len(numbers) - range_length):
            numbers_range = numbers[i : i + range_length]
            if sum(numbers_range) == target:
                return numbers_range


with open("input.txt") as f:
    numbers_input = [
        int(l.strip())
        for l in f
    ]

first_invalid = get_first_invalid(numbers_input)
print(first_invalid)
contiguous_range = get_contiguous_range(numbers_input, first_invalid)
print(min(contiguous_range) + max (contiguous_range))
