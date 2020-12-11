from copy import deepcopy


def find_adjacent_people_pt_1(input_plan, row, column):
    # I can't think of a nicer way to do this without importing some kind of computer vision kernel package
    adjacent_seats = input_plan[row + 1][column + 1] + input_plan[row + 1][column - 1] + \
                     input_plan[row - 1][column + 1] + input_plan[row - 1][column - 1] + input_plan[row + 1][column] + \
                     input_plan[row - 1][column] + input_plan[row][column + 1] + input_plan[row][column - 1]
    return adjacent_seats.count("#")


def find_seating_pt_1(input_plan):
    # similar to game of life, just look at the cells around you and update
    output_plan = deepcopy(input_plan)
    for i in range(1, len(input_plan) - 1):
        for j in range(1, len(input_plan[0]) - 1):
            if input_plan[i][j] == ".":
                continue
            adjacent_people = find_adjacent_people_pt_1(input_plan, i, j)
            if adjacent_people == 0:
                output_plan[i][j] = "#"
            if adjacent_people >= 4:
                output_plan[i][j] = "L"

    return output_plan


def find_adjacent_people_pt_2(input_plan, row, column):
    # this is messy, but this was the most readable thing I could think of, I'm sure python has a way!
    adjacent_seats = ""
    min_row = 0
    min_column = 0
    max_row = len(input_plan)
    max_column = len(input_plan[0])

    # look down
    check_row = row
    while (check_row := check_row - 1) > min_row:
        if input_plan[check_row][column] != ".":
            adjacent_seats += input_plan[check_row][column]
            break

    # look up
    check_row = row
    while (check_row := check_row + 1) < max_row:
        if input_plan[check_row][column] != ".":
            adjacent_seats += input_plan[check_row][column]
            break

    # look left
    check_col = column
    while (check_col := check_col - 1) > min_column:
        if input_plan[row][check_col] != ".":
            adjacent_seats += input_plan[row][check_col]
            break

    # look right
    check_col = column
    while (check_col := check_col + 1) < max_column:
        if input_plan[row][check_col] != ".":
            adjacent_seats += input_plan[row][check_col]
            break

    # look down-left
    check_row = row
    check_col = column
    while (check_row := check_row - 1) > min_row and (check_col := check_col - 1) > min_column:
        if input_plan[check_row][check_col] != ".":
            adjacent_seats += input_plan[check_row][check_col]
            break

    # look down-right
    check_row = row
    check_col = column
    while (check_row := check_row - 1) > min_row and (check_col := check_col + 1) < max_column:
        if input_plan[check_row][check_col] != ".":
            adjacent_seats += input_plan[check_row][check_col]
            break

    # look up-left
    check_row = row
    check_col = column
    while (check_row := check_row + 1) < max_row and (check_col := check_col - 1) > min_column:
        if input_plan[check_row][check_col] != ".":
            adjacent_seats += input_plan[check_row][check_col]
            break

    # look up-right
    check_row = row
    check_col = column
    while (check_row := check_row + 1) < max_row and (check_col := check_col + 1) < max_column:
        if input_plan[check_row][check_col] != ".":
            adjacent_seats += input_plan[check_row][check_col]
            break

    return adjacent_seats.count("#")


def find_seating_pt_2(input_plan):
    # same procedure as part 1
    output_plan = deepcopy(input_plan)
    for i in range(1, len(input_plan) - 1):
        for j in range(1, len(input_plan[0]) - 1):
            if input_plan[i][j] == ".":
                continue
            adjacent_people = find_adjacent_people_pt_2(input_plan, i, j)
            if adjacent_people == 0:
                output_plan[i][j] = "#"
            if adjacent_people >= 5:
                output_plan[i][j] = "L"

    return output_plan


if __name__ == '__main__':
    # this is the longest running program to date, this is because it is O(nm) with m rows and n columns for part 1
    # as well as O(n^2m^2) in the worst case for part 2 (basically assuming no chairs at all)

    # this is a nice homage to John Conway who sadly died this year
    with open("seats.txt", "r") as f:
        seating_plan = [[y for y in f".{x}."] for x in f.read().splitlines()]
    seating_plan.insert(0, ["."] * len(seating_plan[0]))
    seating_plan.append(["."] * len(seating_plan[0]))

    pt_1_plan = deepcopy(seating_plan)
    while (output := find_seating_pt_1(deepcopy(pt_1_plan))) != pt_1_plan:
        pt_1_plan = output

    total = sum(x.count("#") for x in output)

    print(f"Total seats occupied in part 1 is {total}")

    pt_2_plan = deepcopy(seating_plan)
    while (output := find_seating_pt_2(deepcopy(pt_2_plan))) != pt_2_plan:
        pt_2_plan = output

    total = sum(x.count("#") for x in output)

    print(f"Total seats occupied in part 2 is {total}")
