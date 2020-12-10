import math

with open("input.txt") as f:
    boarding_passes = [
        l.strip()
        for l in f
    ]


def binary_read(letters, first_half_letter, second_half_letter):
    start = 0
    end = 2 ** len(letters) - 1

    for letter in letters:
        if letter == first_half_letter:
            end = math.floor((start + end) / 2)
        elif letter == second_half_letter:
            start = math.ceil((start + end) / 2)
        else:
            raise ValueError(letter)

    assert start == end, f"{start} != {end}"
    return start


def get_row(boarding_pass):
    return binary_read(boarding_pass[:7], "F", "B")


def get_column(boarding_pass):
    return binary_read(boarding_pass[7:], "L", "R")


def get_seat_id(boarding_pass):
    return 8 * get_row(boarding_pass) + get_column(boarding_pass)


def get_missing_boarding_pass_id(ids):
    valid_boarding_pass_ids = set(range(max_boarding_pass_ids + 1))
    missing_boarding_pass_ids = valid_boarding_pass_ids - ids
    last_boarding_pass_id = None
    for missing_boarding_pass_id in sorted(missing_boarding_pass_ids):
        if last_boarding_pass_id and abs(missing_boarding_pass_id - last_boarding_pass_id) > 1:
            return missing_boarding_pass_id
        last_boarding_pass_id = missing_boarding_pass_id


boarding_pass_ids = {
    get_seat_id(b)
    for b in boarding_passes
}
max_boarding_pass_ids = max(boarding_pass_ids)

print(max(boarding_pass_ids))
print(get_missing_boarding_pass_id(boarding_pass_ids))

