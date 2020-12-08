def check_pt_1(input_number):
    test = str(input_number)
    for digit in range(1, len(test)):
        if int(test[digit]) < int(test[digit - 1]):
            return False
    if len(set(test)) == len(test):
        return False
    return True


def check_pt_2(input_number):
    test = str(input_number)
    for digit in range(1, len(test)):
        if int(test[digit]) < int(test[digit - 1]):
            return False

    digits = set(test)
    flag = False
    for digit in digits:
        if test.count(digit) == 2:
            flag = True

    if flag:
        return True
    else:
        return False


if __name__ == '__main__':
    input_min = 264793
    input_max = 803935

    total = 0
    for number in range(input_min, input_max + 1):
        if check_pt_1(number):
            total += 1
    print(f"Total for part 1 is {total}")

    total = 0
    for number in range(input_min, input_max + 1):
        if check_pt_2(number):
            total += 1
    print(f"Total for part 2 is {total}")
