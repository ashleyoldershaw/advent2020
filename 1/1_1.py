def find_2_numbers(input):
    # cycle through looking for 2 numbers which add to 2020, then return product
    # O(n^2), it will go through in the worst case (n/2)(n+1) or (n^2 + n)/2
    for i in range(len(input)):
        for j in range(i, len(input)):
            if input[i] + input[j] == 2020:
                return input[i] * input[j]


def find_3_numbers(input):
    # cycle through looking for 3 numbers which add to 2020, then return product
    # O(n^3)
    for i in range(len(input)):
        for j in range(i, len(input)):
            for k in range(j, len(input)):
                if input[i] + input[j] + input[k] == 2020:
                    return input[i] * input[j] * input[k]


if __name__ == '__main__':
    # read in the file and convert everything to integers
    with open("expenses.txt", "r") as f:
        entries = [int(entry) for entry in f.read().split()]

    product = find_2_numbers(entries)
    print(f"The first number HR wants is {product}")

    product = find_3_numbers(entries)
    print(f"The second number HR wants is {product}")
