with open("input.txt") as f:
    initial_seats = [
        line.strip()
        for line in f
    ]
width = len(initial_seats[0])
height = len(initial_seats)


def adjacent(j, i, seats):
    return [
        seats[y][x]
        for y in range(j - 1, j + 2)
        for x in range(i - 1, i + 2)
        if (y != j or x != i) and 0 <= y < height and 0 <= x < width
    ]


def next_state_p1(seats):
    new_state = []
    for j in range(height):
        new_row = []
        for i in range(width):
            seat = seats[j][i]
            adjacent_seats = adjacent(j, i, seats)
            occupied = sum(s == "#" for s in adjacent_seats)
            if seat == "L" and occupied == 0:
                new_row.append("#")
            elif seat == "#" and occupied >= 4:
                new_row.append("L")
            else:
                new_row.append(seat)
        new_state.append(new_row)
    return new_state


def part_1(seats):
    last_state = seats
    while True:
        new_state = next_state_p1(last_state)
        if new_state == last_state:
            return new_state
        last_state = new_state


def first_visible(j, i, v, u, seats):
    y = j + v
    x = i + u
    while 0 <= y < height and 0 <= x < width:
        if seats[y][x] != ".":
            return seats[y][x]
        y += v
        x += u
    return None


def visible(j, i, seats):
    return [
        s
        for s in [
            first_visible(j, i, v, u, seats)
            for v in range(-1, 2)
            for u in range(-1, 2)
            if v != 0 or u != 0
        ]
        if s is not None
    ]


def next_state_p2(seats):
    new_state = []
    for j in range(height):
        new_row = []
        for i in range(width):
            seat = seats[j][i]
            visible_seats = visible(j, i, seats)
            occupied = sum(s == "#" for s in visible_seats)
            if seat == "L" and occupied == 0:
                new_row.append("#")
            elif seat == "#" and occupied >= 5:
                new_row.append("L")
            else:
                new_row.append(seat)
        new_state.append(new_row)
    return new_state


def part_2(seats):
    last_state = seats
    while True:
        new_state = next_state_p2(last_state)
        if new_state == last_state:
            return new_state
        last_state = new_state


final_seats_p1 = part_1(initial_seats)
print(sum(
    final_seats_p1[j][i] == "#"
    for j in range(height)
    for i in range(width)
))

final_seats_p2 = part_2(initial_seats)
print(sum(
    final_seats_p2[j][i] == "#"
    for j in range(height)
    for i in range(width)
))
