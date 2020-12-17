INPUT = "2,0,6,12,1,3"
INPUT_NUMBERS = [
    int(n)
    for n in INPUT.split(",")
]


def get_next_state(state, turn, last_number):
    if last_number not in state:
        new_number = 0
    else:
        new_number = turn - 1 - state[last_number]
    state[last_number] = turn - 1
    return state, new_number


def get_nth_number(numbers, n):
    state = {
        n: i
        for i, n in enumerate(numbers[:-1])
    }
    turn = len(numbers)
    last_number = numbers[-1]
    while turn < n:
        if turn % 1_000_000 == 0:
            print(f"{turn / n:.0%}")
        state, last_number = get_next_state(state, turn, last_number)
        turn += 1
    return last_number


print(get_nth_number(INPUT_NUMBERS, 2020))
print(get_nth_number(INPUT_NUMBERS, 30_000_000))
