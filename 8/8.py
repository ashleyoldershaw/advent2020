import copy


def find_acc_value_before_loop(input_program):
    accumulator = 0
    location = 0
    while True:
        command = input_program[location]

        if command["executed"]:
            return accumulator

        if command["command"] == "nop":
            location += 1
        elif command["command"] == "acc":
            accumulator += command["value"]
            location += 1
        elif command["command"] == "jmp":
            location += command["value"]
        else:
            raise RuntimeError("Strange command!")

        command["executed"] = True


def execute_program(input_program):
    accumulator = 0
    location = 0
    while True:
        if 0 <= location < len(input_program):
            command = input_program[location]
        elif location == len(input_program):
            return accumulator
        else:
            return False

        if command["executed"]:
            return False

        if command["command"] == "nop":
            location += 1
        elif command["command"] == "acc":
            accumulator += command["value"]
            location += 1
        elif command["command"] == "jmp":
            location += command["value"]
        else:
            raise RuntimeError("Strange command!")

        command["executed"] = True


def flip_op_to_avoid_loop(input_program):
    # start by flipping jmps to nops
    print("Flipping jumps to nops")
    flips = [cmd for cmd in input_program if cmd["command"] == "jmp"]
    for flip in flips:
        flip["command"] = "nop"
        if (program_output := execute_program(copy.deepcopy(input_program))) != False:
            return program_output
        else:
            flip["command"] = "jmp"

    print("Flipping nops to jumps")
    flips = [cmd for cmd in input_program if cmd["command"] == "nop"]
    for flip in flips:
        flip["command"] = "jmp"
        if (program_output := execute_program(copy.deepcopy(input_program))) != False:
            return program_output
        else:
            flip["command"] = "nop"

    return 0


if __name__ == '__main__':
    with open("program.txt", "r") as f:
        program = [{"command": x.split()[0], "value": int(x.split()[1]), "executed": False} for x in
                   f.read().splitlines()]

    output = find_acc_value_before_loop(copy.deepcopy(program))

    print(f"Accumulator value before loop is {output}")

    output = flip_op_to_avoid_loop(copy.deepcopy(program))
    print(f"Accumulator value after program termination is {output}")
