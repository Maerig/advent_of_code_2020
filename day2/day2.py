import re

PASSWORD_REGEX = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")


def parse_password(raw_password):
    match = PASSWORD_REGEX.match(raw_password.strip())
    x, y, letter, word = match.groups()
    return int(x), int(y), letter, word


def is_valid_password_p1(min_count, max_count, letter, word):
    return min_count <= word.count(letter) <= max_count


def is_valid_password_p2(i, j, letter, word):
    return (word[i - 1] == letter) != (word[j - 1] == letter)


with open("input.txt") as f:
    passwords = [
        parse_password(line)
        for line in f
    ]


print(sum(
    is_valid_password_p1(x, y, letter, word)
    for x, y, letter, word in passwords
))


print(sum(
    is_valid_password_p2(x, y, letter, word)
    for x, y, letter, word in passwords
))