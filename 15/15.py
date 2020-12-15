def get_number_at_turn(sequence, turn_to_end):
    # luckily I completed both parts in one!
    # By adding a turn_to_end variable it allowed me to work out the numbers for parts 1 and 2
    number_dicts = {}

    # populate with the initial sequence
    for i in range(len(sequence) - 1):
        number_dicts[sequence[i]] = {"last_time": i + 1}

    # current number variable should be initialised to the first value in the loop
    current_number = sequence[-1]

    starting_turn = len(sequence) + 1
    for turn in range(starting_turn, turn_to_end + 1):
        if current_number in number_dicts:
            # if we have an existing number, swap the values and calculate the current_number value
            number_dicts[current_number]["second_to_last_time"] = number_dicts[current_number]["last_time"]
            number_dicts[current_number]["last_time"] = turn - 1
            current_number = number_dicts[current_number]["last_time"] - \
                             number_dicts[current_number]["second_to_last_time"]
        else:
            # if we don't have the number yet, initialise it, the current number is then 0
            number_dicts[current_number] = {"last_time": turn - 1}
            current_number = 0

    return current_number


if __name__ == '__main__':
    input_sequence = 0, 1, 4, 13, 15, 12, 16

    part_1_ans = get_number_at_turn(input_sequence, 2020)
    print(f"2020th number in sequence is {part_1_ans}")

    # this second one takes a little longer, but still works fine
    part_2_ans = get_number_at_turn(input_sequence, 30000000)
    print(f"30000000th number in sequence is {part_2_ans}")
