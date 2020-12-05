def count_trees_pt_1(entries):
    # initially specialised for the spec, I just kept this for fun as I didn't know for sure what was going to happen
    # (KISS principle!)
    location = 0
    count = 0
    for line in entries:
        if line[location] == "#":
            count += 1
        location = (location + 3) % len(line)

    return count


def count_trees(entries, right_offset, down_offset):
    # a more flexible option
    row = 0
    col = 0
    count = 0
    while row < len(entries):
        if entries[row][col] == "#":
            count += 1
        col = (col + right_offset) % len(entries[row])
        row += down_offset

    return count


if __name__ == '__main__':
    with open("forest.txt", "r") as f:
        forest = f.read().splitlines()

    total = count_trees_pt_1(forest)
    print(f"You hit {total} trees in part 1!")

    # for part 2 we have this!
    """
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    """
    total = count_trees(forest, 1, 1) * count_trees(forest, 3, 1) * count_trees(forest, 5, 1) * \
            count_trees(forest, 7, 1) * count_trees(forest, 1, 2)

    print(f"The product for part 2 is {total}")
