import math

import numpy as np


def part_1(timetable_lines):
    current_timestamp = int(timetable_lines[0])
    timetable = [int(x) for x in timetable_lines[1].split(",") if x != "x"]

    # use some nice dictionary comprehension
    time_to_wait = {bus: (bus - (current_timestamp % bus)) for bus in timetable}

    # find the bus to catch and return the product
    bus_to_catch = min(time_to_wait, key=lambda bus: time_to_wait[bus])
    return bus_to_catch * time_to_wait[bus_to_catch]


def part_2(timetable_lines):
    # this is a terrible brute force solution that has been running for hours while I try to implement the chinese
    # remainder theorem
    timetable = [int(x) if x != "x" else x for x in timetable_lines[1].split(",")]

    timetable = {timetable.index(x): x for x in timetable if x != "x"}

    max_number_position = max(timetable, key=lambda x: timetable[x])
    max_number = timetable[max_number_position]

    check_timestamp = max_number - max_number_position

    while True:
        match = True
        for position in timetable:
            if ((check_timestamp + position) % timetable[position]) != 0:
                match = False
                break
        if match:
            return check_timestamp
        else:
            check_timestamp += max_number
            if check_timestamp % 1000000000 == 0:
                print(check_timestamp)


def solution_robinhouston(timetable_lines):
    # this is tricky because you can't really brute force it for the main event
    # I spent way too long trying to implement the chinese remainder theorem, see below
    # https://brilliant.org/wiki/chinese-remainder-theorem/#theorem-and-proof
    # in the end I looked on Reddit and found this incredible solution by u/robinhouston who did both parts in  in 150
    # characters which is incredible, I figured if I couldn't work it out myself in a reasonable time I'd showcase a
    # great solution on here

    i = x = 0
    T, D = map(eval, open("timetable.txt"))
    r = n = 1
    for b in D:
        if b: r, n = (-n * (i + r) * pow(n, -1, b) + r) % (n * b), n * b
        i += 1
    return min({(-T % b, -T % b * b) for b in D if b})[1], r


if __name__ == '__main__':
    with open("timetable.txt", "r") as f:
        text = f.read().splitlines()

    part_1_answer = part_1(text)
    print(f"In part 1, answer is {part_1_answer}")

    part_2_answer = solution_robinhouston(text)[1]
    print(f"In part 2, answer is {part_2_answer}")
