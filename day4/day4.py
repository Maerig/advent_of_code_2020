import re


REQUIRED_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]


passports = []
with open("input.txt") as f:
    current_passport = {}
    for l in f:
        if l == "\n":
            passports.append(current_passport)
            current_passport = {}
        for entry in l.strip().split():
            k, v = entry.split(":")
            current_passport[k] = v
    if current_passport:
        passports.append(current_passport)


def is_valid_passport_p1(passport):
    return all(
        field in passport
        for field in REQUIRED_FIELDS
    )


def is_valid_height(height):
    match = re.match(r"^(\d+)(cm|in)$", height)
    if not match:
        return False
    value, unit = match.groups()
    if unit == "cm":
        return 150 <= int(value) <= 193
    if unit == "in":
        return 59 <= int(value) <= 76
    raise ValueError(unit)


def is_valid_hair_colour(eye_colour):
    return re.match(r"^#[0-9a-f]{6}$", eye_colour) is not None


def is_valid_eye_colour(eye_colour):
    return eye_colour in {
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth"
    }


def is_valid_pid(pid):
    return re.match(r"^\d{9}$", pid) is not None

def is_valid_passport_p2(passport):
    return all([
        1920 <= int(passport["byr"]) <= 2002,
        2010 <= int(passport["iyr"]) <= 2020,
        2020 <= int(passport["eyr"]) <= 2030,
        is_valid_height(passport["hgt"]),
        is_valid_hair_colour(passport["hcl"]),
        is_valid_eye_colour(passport["ecl"]),
        is_valid_pid(passport["pid"]),
    ])


print(sum(
    is_valid_passport_p1(p)
    for p in passports
))


print(sum(
    is_valid_passport_p2(p)
    for p in passports
    if is_valid_passport_p1(p)
))
