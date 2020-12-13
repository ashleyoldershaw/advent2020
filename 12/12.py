from copy import deepcopy

import numpy as np


def calculate_manhattan_distance_pt_1(instructions, initial_direction):
    compass = ["N", "E", "S", "W"]
    compass_index = compass.index(initial_direction)

    distance_travelled = {"N": 0, "E": 0, "S": 0, "W": 0}

    for instruction in instructions:
        if instruction["direction"] == "F":
            instruction["direction"] = compass[compass_index]

        if instruction["direction"] == "R":
            compass_index = (compass_index + int(instruction["distance"] / 90)) % 4
        elif instruction["direction"] == "L":
            compass_index = (compass_index - int(instruction["distance"] / 90)) % 4
        else:
            distance_travelled[instruction["direction"]] += instruction["distance"]

    return abs(distance_travelled["N"] - distance_travelled["S"]) + \
           abs(distance_travelled["E"] - distance_travelled["W"])


def calculate_manhattan_distance_pt_2(instructions, waypoint_location):
    # most of this is quite simple apart from the rotation, thankfully we can easily use some matrices to calculate this
    distance_travelled = np.array([0, 0])

    for instruction in instructions:
        if instruction["direction"] == "F":
            distance_travelled += waypoint_location * instruction["distance"]
        elif instruction["direction"] == "E":
            waypoint_location[0] += instruction["distance"]
        elif instruction["direction"] == "W":
            waypoint_location[0] -= instruction["distance"]
        elif instruction["direction"] == "N":
            waypoint_location[1] += instruction["distance"]
        elif instruction["direction"] == "S":
            waypoint_location[1] -= instruction["distance"]

        else:
            rotation_scale = 1 if instruction["direction"] == "L" else -1
            rotation = instruction["distance"] * rotation_scale
            theta = np.radians(rotation)
            c, s = np.cos(theta), np.sin(theta)
            rotation_matrix = np.round(np.array(((c, -s), (s, c)))).astype(int)

            waypoint_location = rotation_matrix.dot(waypoint_location)

    return abs(distance_travelled[0]) + abs(distance_travelled[1])


if __name__ == '__main__':
    with open("directions.txt", "r") as f:
        directions = [{"direction": x[0], "distance": int(x[1:])} for x in f.read().splitlines()]

    manhattan_distance = calculate_manhattan_distance_pt_1(deepcopy(directions), "E")
    print(f"Manhattan distance for pt 1 is {manhattan_distance}")

    manhattan_distance = calculate_manhattan_distance_pt_2(deepcopy(directions), np.array([10, 1]))
    print(f"Manhattan distance for pt 2 is {manhattan_distance}")
