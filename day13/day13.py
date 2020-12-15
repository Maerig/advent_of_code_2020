with open("input.txt") as f:
    start_time = int(next(f).strip())
    buses = [
        int(n) if n != "x" else None
        for n in next(f).strip().split(",")
    ]


def waiting_time(bus_id, t):
    elapsed_time = t % bus_id
    return bus_id - elapsed_time if elapsed_time != 0 else 0


def part_1(start_time, buses):
    waiting_times = (
        (bus_id, waiting_time(bus_id, start_time))
        for bus_id in buses
        if bus_id
    )
    earliest_id, earliest_time = min(waiting_times, key=lambda wt: wt[1])
    return earliest_id * earliest_time


def part_2(buses):
    bus_times = [
        (bus_id, bus_id - i)
        for i, bus_id in enumerate(buses)
        if bus_id
    ]
    while True:
        _, first_bus_time = bus_times[0]
        if all(
            bus_time == first_bus_time
            for _, bus_time in bus_times[1:]
        ):
            return first_bus_time
        # Else advance earliest
        earliest_idx, earliest_bus_id, earliest_bus_time = min((
            (i, bus_id, bus_time)
            for i, (bus_id, bus_time) in enumerate(bus_times)
        ), key=lambda idx_id_time: idx_id_time[2])
        bus_times[earliest_idx] = (earliest_bus_id, earliest_bus_time + earliest_bus_id)


print(part_1(start_time, buses))
print(part_2(buses))
