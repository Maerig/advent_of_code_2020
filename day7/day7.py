import re

RULE_REGEX = re.compile(r"^(.+) bags contain (.+)\.$")
CONTAINED_BAGS_REGEX = re.compile(r"(\d)+ (.+) bags?")


rules = {}
with open("input.txt") as f:
    for l in f:
        match = RULE_REGEX.match(l)
        if not match:
            raise ValueError(l)

        colour, tail = match.groups()
        rules[colour] = []
        if tail == "no other bags":
            continue

        contained_bags = tail.split(", ")
        for contained_bag in contained_bags:
            match = CONTAINED_BAGS_REGEX.match(contained_bag)
            if not match:
                raise ValueError(contained_bag)

            contained_count, contained_colour = match.groups()
            rules[colour].append((int(contained_count), contained_colour))


def can_contain_one(container, target, containing_rules):
    return any(
        contained == target or can_contain_one(contained, target, containing_rules)
        for _, contained in containing_rules[container]
    )


def must_contain(container, containing_rules):
    return sum(
        count + count * must_contain(contained, containing_rules)
        for count, contained in containing_rules[container]
    )



print(sum(
    can_contain_one(colour, "shiny gold", rules)
    for colour in rules
))
print(must_contain("shiny gold", rules))

