def count_character_passwords(entries):
    # count all the passwords that have enough characters match
    count_total = 0

    for row in entries:
        info = row.split()
        lower, upper = [int(x) for x in info[0].split("-")[:]]
        character = info[1][0]
        char_count = info[2].count(character)
        if lower <= char_count <= upper:
            count_total += 1

    return count_total


def count_positional_passwords(entries):
    # count all the passwords that have one character match in one position and not the other
    count_total = 0

    for row in entries:
        info = row.split()
        lower, upper = [int(x) for x in info[0].split("-")[:]]
        character = info[1][0]
        # xor returns true if one is true and the other is not, could also use != but xor is fun
        if (info[2][lower - 1] == character) ^ (info[2][upper - 1] == character):
            count_total += 1

    return count_total


if __name__ == '__main__':
    with open("passwords.txt", "r") as f:
        rows = f.read().splitlines()

    total = count_character_passwords(rows)
    print(f"Initial total count is {total}")

    total = count_positional_passwords(rows)
    print(f"Second total count is {total}")
