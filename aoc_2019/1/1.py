def calculate_total_fuel_pt_1(inputs):
    total = 0
    for i in inputs:
        total += int(i / 3) - 2
    return total


def calculate_total_fuel_pt_2(inputs):
    total = 0
    for i in inputs:
        fuel = i
        while True:
            fuel = int(fuel / 3) - 2
            if fuel > 0:
                total += fuel
            else:
                break
    return total


if __name__ == '__main__':
    with open("modules.txt", "r") as f:
        weights = [int(x) for x in f.read().splitlines()]

    print(f"Total for pt.1 is: {calculate_total_fuel_pt_1(weights)}")

    print(f"Total for pt.2 is: {calculate_total_fuel_pt_2(weights)}")
