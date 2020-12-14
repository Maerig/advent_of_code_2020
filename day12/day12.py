import re


DIRECTIONS = ["N", "E", "S", "W"]
INSTRUCTION_REGEX = re.compile(r"^([NSEWLRF])(\d+)$")


def parse_instructions(path):
    with open(path) as f:
        for line in f:
            match = INSTRUCTION_REGEX.match(line.strip())
            if not match:
                raise ValueError(line)
            action, units = match.groups()
            yield action, int(units)


class Ship:
    def __init__(self):
        self.direction = "E"
        self.x = 0
        self.y = 0

    def execute(self, action, units):
        if action in DIRECTIONS:
            self.move(action, units)
        elif action == "R":
            self.turn(1, units)
        elif action == "L":
            self.turn(-1, units)
        elif action == "F":
            self.move(self.direction, units)

    def move(self, direction, units):
        if direction == "N":
            self.y += units
        elif direction == "E":
            self.x += units
        elif direction == "S":
            self.y -= units
        elif direction == "W":
            self.x -= units
        else:
            raise ValueError(direction)

    def turn(self, multiplier, units):
        current_index = DIRECTIONS.index(self.direction)
        new_index = int(current_index + multiplier * units / 90) % len(DIRECTIONS)
        self.direction = DIRECTIONS[new_index]


def part_1(instructions):
    ship = Ship()
    for action, units in instructions:
        ship.execute(action, units)
    return abs(ship.x) + abs(ship.y)


class ShipMkII:
    def __init__(self):
        self.direction = "E"
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1

    def execute(self, action, units):
        if action in DIRECTIONS:
            self.move_waypoint(action, units)
        elif action == "R":
            self.rotate_waypoint(1, units)
        elif action == "L":
            self.rotate_waypoint(-1, units)
        elif action == "F":
            self.move_forward(units)

    def move_waypoint(self, direction, units):
        if direction == "N":
            self.waypoint_y += units
        elif direction == "E":
            self.waypoint_x += units
        elif direction == "S":
            self.waypoint_y -= units
        elif direction == "W":
            self.waypoint_x -= units
        else:
            raise ValueError(direction)

    def rotate_waypoint(self, direction, units):
        for _ in range(units // 90):
            self.waypoint_x, self.waypoint_y = direction * self.waypoint_y, -direction * self.waypoint_x

    def move_forward(self, units):
        self.x += units * self.waypoint_x
        self.y += units * self.waypoint_y


def part_2(instructions):
    ship = ShipMkII()
    for action, units in instructions:
        ship.execute(action, units)
    return abs(ship.x) + abs(ship.y)


instructions_input = list(parse_instructions("input.txt"))
print(part_1(instructions_input))
print(part_2(instructions_input))
