from copy import copy


def calculate_sum_total_of_memory_pt_1(input_memory):
    instructions = {group.splitlines()[0]: {mem_value.split(" = ")[0]: int(mem_value.split(" = ")[1]) for mem_value in
                                            group.splitlines()[1:]} for group in input_memory.split("mask = ")[1:]}
    memory = {}
    for mask in instructions:
        for mem_value in instructions[mask]:
            string = f"{instructions[mask][mem_value]:036b}"

            memory[mem_value] = int("".join(string[i] if mask[i] == "X" else mask[i] for i in range(len(mask))), 2)

    return sum(memory.values())


def get_memory_values(input_string, bitmask, storage_list, pos):
    for i in range(pos, len(input_string)):
        if bitmask[i] == "1":
            input_string[i] = "1"
        elif bitmask[i] == "X":
            input_string[i] = "0"
            get_memory_values(copy(input_string), bitmask, storage_list, i + 1)
            input_string[i] = "1"

            get_memory_values(copy(input_string), bitmask, storage_list, i + 1)
            return storage_list

    storage_list.append(int("".join(input_string), 2))
    return storage_list


def calculate_sum_total_of_memory_pt_2(input_memory):
    instructions = {
        group.splitlines()[0]: {int(mem_value.split(" = ")[0].strip("mem[]")): int(mem_value.split(" = ")[1]) for
                                mem_value in group.splitlines()[1:]} for group in input_memory.split("mask = ")[1:]}
    memory = {}
    for mask in instructions:
        for mem_value in instructions[mask]:
            mem_locations = []
            string = list(f"{mem_value:036b}")
            values = get_memory_values(string, mask, mem_locations, 0)
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
