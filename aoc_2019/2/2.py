def intcode_computer(program):
    for i in range(0, len(program), 4):
        if program[i] == 99:
            break

        op = program[i]
        number1 = program[program[i + 1]]
        number2 = program[program[i + 2]]
        save_loc = program[i + 3]

        if op == 1:
            program[save_loc] = number1 + number2
        elif op == 2:
            program[save_loc] = number1 * number2
        else:
            raise RuntimeError(f"Invalid operator! {op}")

    return program


def find_noun_and_verb(input_program):
    goal = 19690720

    # brute force time, could probably do some kind of heuristic search or something
    for i in range(100):
        for j in range(100):
            new_program = input_program.copy()
            new_program[1] = i
            new_program[2] = j
            if intcode_computer(new_program)[0] == goal:
                print(f"Part 2: Noun * 100 + verb = {i * 100 + j}")
                break


if __name__ == '__main__':
    with open("program_1.txt", "r") as f:
        input_1 = [int(x) for x in f.read().split(',')]

    output = intcode_computer(input_1)

    print(f"The value at position 0 after the end of part 1 is {output[0]}")

    with open("program_2.txt", "r") as f:
        input_2 = [int(x) for x in f.read().split(',')]

    find_noun_and_verb(input_2)
