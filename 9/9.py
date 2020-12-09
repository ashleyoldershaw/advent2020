def find_number_not_matching_pattern(numbers):
    # this is an improvement of the brute force tactic done in day 1
    # this idea was mentioned to me as a solution for day 1 by the lovely oskar holm
    size = 25

    for i in range(size, len(numbers) - 1):
        preamble = sorted(numbers[i - size:i])
        target = numbers[i]

        upper = size - 1
        lower = 0

        found = False

        # use the sorted range, add together the upper and lower bounds and if it's too big choose a smaller number
        # if it's too small choose a bigger number
        while upper != lower:
            temp = preamble[lower] + preamble[upper]

            if temp == target:
                found = True
                break
            elif temp > target:
                upper -= 1
            elif temp < target:
                lower += 1

        # the while loop will end if we find the number or if we don't
        # so we have a flag here to return when we don't find the number
        if not found:
            return target


def find_contiguous_set_of_numbers(target, numbers):
    # there's absolutely no way I was going to brute force this, so I thought of a caterpillar sort of solution where
    # we slide up the set, checking to see if they add up, and if they don't then raise or lower the total amount in
    # the range, always going forwards
    upper = 1
    lower = 0
    while (total := sum(numbers[lower:upper])) != target:
        if total > target:
            lower += 1
        elif total < target:
            upper += 1

    return numbers[lower:upper]


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        input_numbers = [int(x) for x in f.read().splitlines()]

    invalid_number = find_number_not_matching_pattern(input_numbers)

    print(f"First number not matching pattern is {invalid_number}")

    output = find_contiguous_set_of_numbers(invalid_number, input_numbers)

    print(f"Answer to part 2 is {min(output) + max(output)}")
