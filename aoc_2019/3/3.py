def find_closest_intersection_manhattan(wire_instructions):
    wire_locations = []

    for wire in wire_instructions:
        x = 0
        y = 0
        co_ords = set()
        for bend in wire:
            length = bend[1]
            if bend[0] == "R":
                for i in range(length):
                    x += 1
                    co_ords.add((x, y))
            if bend[0] == "L":
                for i in range(length):
                    x -= 1
                    co_ords.add((x, y))
            if bend[0] == "U":
                for i in range(length):
                    y += 1
                    co_ords.add((x, y))
            if bend[0] == "D":
                for i in range(length):
                    y -= 1
                    co_ords.add((x, y))

        wire_locations.append(co_ords)

    return set.intersection(*wire_locations)


def find_closest_intersection_time(wire_instructions):
    # we can just step along both wires until we find an intersection
    wire_dict = {"a": {"instructions": wire_instructions[0], "length": 0, "x": 0, "y": 0},
                 "b": {"instructions": wire_instructions[1], "length": 0, "x": 0, "y": 0}}

    # format will be like this {(0, 0): {"a": 0,"b": 0}}
    distances = {}
    combined_crossover_lengths = []

    while True:
        wire_to_grow = min(wire_dict, key=lambda x: wire_dict[x]["length"])
        if not wire_dict[wire_to_grow]["instructions"]:
            wire_to_grow = 'b' if wire_to_grow == 'a' else 'a'

        if not wire_dict[wire_to_grow]["instructions"]:
            return min(combined_crossover_lengths)

        instruction = wire_dict[wire_to_grow]["instructions"].pop(0)

        direction = instruction[0]
        length = instruction[1]

        for i in range(length):
            if direction == "R":
                wire_dict[wire_to_grow]["x"] += 1
            if direction == "L":
                wire_dict[wire_to_grow]["x"] -= 1
            if direction == "U":
                wire_dict[wire_to_grow]["y"] += 1
            if direction == "D":
                wire_dict[wire_to_grow]["y"] -= 1

            wire_dict[wire_to_grow]["length"] += 1

            co_ords = wire_dict[wire_to_grow]["x"], wire_dict[wire_to_grow]["y"]

            if co_ords in distances:
                if wire_to_grow not in distances[co_ords]:
                    # means we found a crossover!
                    # add the combined lengths to the combined crossover length list
                    other_wire = 'b' if wire_to_grow == 'a' else 'a'
                    combined_crossover_lengths.append(
                        wire_dict[wire_to_grow]["length"] + distances[co_ords][other_wire])

                    distances[co_ords] = {wire_to_grow: wire_dict[wire_to_grow]["length"]}
            else:
                distances[co_ords] = {wire_to_grow: wire_dict[wire_to_grow]["length"]}


if __name__ == '__main__':
    with open("wires.txt", "r") as f:
        wires = [[[x[0], int(x[1:])] for x in line.split(",")] for line in f.read().splitlines()]

    intersections = find_closest_intersection_manhattan(wires)

    closest_crossover = min(intersections, key=lambda x: abs(x[0]) + abs(x[1]))

    print(f"Closest crossover is {abs(closest_crossover[0]) + abs(closest_crossover[1])} units away")

    time = find_closest_intersection_time(wires)
    print(f"Combined wire length to first crossover is {time}")
