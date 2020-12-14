from copy import copy


def calculate_sum_total_of_memory_pt_1(input_memory):
    # this function works with bit masking, where the mask overwrites the value at each memory location
    # with wildcard values marked by X
    # eg mask of 0XX1 on value 1010 would give a value of 0011

    # the requirement is that we add up all the values in the memory dictionary at the end, so we return an int

    # we split up the input into groups, with dictionaries in the following format
    # {
    #     mask1: {location1: value1, location2: value2},
    #     mask2: {location3: value3, location4: value4}
    # }
    instructions = {group.splitlines()[0]: {mem_value.split(" = ")[0]: int(mem_value.split(" = ")[1]) for mem_value in
                                            group.splitlines()[1:]} for group in input_memory.split("mask = ")[1:]}
    memory = {}
    for mask, value in instructions.items():
        for mem_value in value:
            # convert the value to a binary string
            string = f"{instructions[mask][mem_value]:036b}"
            # apply the bitmask here to generate the new integer
            memory[mem_value] = int("".join(string[i] if mask[i] == "X" else mask[i] for i in range(len(mask))), 2)

    # now we can sum the values from the memory dict to give the final answer
    return sum(memory.values())


def get_memory_values(input_string, bitmask, storage_list, pos):
    # recursive function to find all the memory locations required in part 2
    for i in range(pos, len(input_string)):
        if bitmask[i] == "1":
            # a value of 1 in the bitmask always overwrites the input string value to a 1, regardless of what it was
            input_string[i] = "1"
        elif bitmask[i] == "X":
            # a value of X in the bitmask means we need to account for both possibilities, so we have recursion in here
            # to add to the list the values at the end
            input_string[i] = "0"
            get_memory_values(copy(input_string), bitmask, storage_list, i + 1)
            input_string[i] = "1"

            get_memory_values(copy(input_string), bitmask, storage_list, i + 1)
            return storage_list

    # we only get to the end of the string in the base case, so we know that there are no wildcard values left
    storage_list.append(int("".join(input_string), 2))
    return storage_list


def calculate_sum_total_of_memory_pt_2(input_memory):
    # the second part is a little more complex, we need to write the value in the dictionary to all possible memory
    # locations, an X in the bitmask means that we need to write to memory locations where that X is a 0 and a 1
    # so we write to 2^n locations where n is the number of Xs in the bitmask

    # the requirement is still that we add up all the values in the memory dictionary at the end, so we return an int

    # we split up the input into groups, with dictionaries in the following format
    # {
    #     mask1: {location1: value1, location2: value2},
    #     mask2: {location3: value3, location4: value4}
    # }
    instructions = {
        group.splitlines()[0]: {int(mem_value.split(" = ")[0].strip("mem[]")): int(mem_value.split(" = ")[1]) for
                                mem_value in group.splitlines()[1:]} for group in input_memory.split("mask = ")[1:]}
    memory = {}
    for mask, value_ in instructions.items():
        for mem_value in value_:
            mem_locations = []
            values = get_memory_values(list(f"{mem_value:036b}"), mask, mem_locations, 0)
            for value in values:
                memory[value] = instructions[mask][mem_value]

    return sum(memory.values())


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        input_data = f.read()

    total = calculate_sum_total_of_memory_pt_1(input_data)
    print(f"Sum of values in memory for part 1: {total}")

    total = calculate_sum_total_of_memory_pt_2(input_data)
    print(f"Sum of values in memory for part 2: {total}")
