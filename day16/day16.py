import re
from functools import reduce

RANGE_RULE_REGEX = re.compile(r"^([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)$")


def parse_input(path):
    with open(path) as f:
        it = iter(f)

        range_rules = []
        while (line := next(it)) != "\n":
            match = RANGE_RULE_REGEX.match(line.strip())
            if not match:
                raise ValueError(line)
            field, x1, x2, y1, y2 = match.groups()
            range_rules.append((field, int(x1), int(x2), int(y1), int(y2)))

        next_line = next(it)
        assert next_line.strip() == "your ticket:"
        own_ticket = [
            int(n)
            for n in next(it).strip().split(",")
        ]

        next(it)
        next_line = next(it)
        assert next_line.strip() == "nearby tickets:"
        nearby_tickets = []
        while line := next(it, None):
            nearby_ticket = [
                int(n)
                for n in line.strip().split(",")
            ]
            nearby_tickets.append(nearby_ticket)

        return range_rules, own_ticket, nearby_tickets


def is_valid(n, x1, x2, y1, y2):
    return x1 <= n <= x2 or y1 <= n <= y2


def part_1(range_rules, nearby_tickets):
    return sum(
        next(
            (
                field
                for field in ticket
                if all(
                    not is_valid(field, x1, x2, y1, y2)
                    for _, x1, x2, y1, y2 in range_rules
                )
            ),
            0
        )
        for ticket in nearby_tickets
    )


def solve_field_names(names, possible_fields):
    field_count = len(names)
    confirmed = set()
    remaining = possible_fields

    while True:
        intersection = [
            [
                name
                for name in names
                if all(
                    name in ticket[i]
                    for ticket in remaining
                )
            ]
            for i in range(field_count)
        ]
        if len(confirmed) == field_count:
            return [
                possible_names[0]
                for possible_names in intersection
            ]

        for i, candidates in enumerate(intersection):
            if len(candidates) > 1:
                continue
            name = candidates[0]
            if name in confirmed:
                continue
            remaining = [
                [
                    [
                        field_name
                        for field_name in field_names
                        if (field_idx == i) == (field_name == name)
                    ]
                    for field_idx, field_names in enumerate(ticket)
                ]
                for ticket in remaining
            ]
            confirmed.add(name)


def part_2(range_rules, own_ticket, nearby_tickets):
    valid_tickets = (
        ticket
        for ticket in nearby_tickets
        if all(
            any(
                is_valid(field, x1, x2, y1, y2)
                for _, x1, x2, y1, y2 in range_rules
            )
            for field in ticket
        )
    )

    names = [
        rule[0]
        for rule in range_rules
    ]
    possible_fields = [
        [
            [
                name
                for name, x1, x2, y1, y2 in range_rules
                if is_valid(field, x1, x2, y1, y2)
            ]
            for field in ticket
        ]
        for ticket in valid_tickets
    ]
    field_names = solve_field_names(names, possible_fields)

    departure_values = (
        value
        for i, value in enumerate(own_ticket)
        if field_names[i].startswith("departure")
    )
    return reduce(lambda x, y: x * y, departure_values)


rules, own, nearby = parse_input("input.txt")
print(part_1(rules, nearby))
print(part_2(rules, own, nearby))
