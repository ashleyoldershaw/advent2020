def find_seat_id(seat):
    # the F and B values are analogous to 0 and 1 values on a binary number, same with the L and R values
    # we want to convert the pass to a binary string, and then convert that to a number
    row_id = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
    col_id = int(seat[7:].replace("L", "0").replace("R", "1"), 2)

    seat_id = row_id * 8 + col_id
    return seat_id


def find_highest_seat_id(passes):
    # find the pass with the highest ID and then get the ID from it
    max_id_pass = max(passes, key=lambda x: find_seat_id(x))
    seat_id = find_seat_id(max_id_pass)
    return seat_id


def find_seat(seats):
    # there is definitely a case to just go through it once and find the missing number
    # but I wanted to do a binary search for fun
    initial_offset = seats[0]
    i = 0
    offset = 0

    while True:
        # check the entry at the pivot is equal to the initial offset + the offset from previous rounds + the pivot
        # if it is, then we know the missing seat number is yet to come, if not, we know we've gone past it
        # iterate through until we reach the base case of pivot = 0, halving the pivot size each round
        i += 1
        pivot = int(len(seats) / 2 ** i)

        # if we find that we haven't gone far enough, add the pivot size to the offset
        if seats[offset + pivot] == initial_offset + offset + pivot:
            offset += pivot

        # we should reach this after log[2](n) where n is the number of seats in the list
        if pivot == 0:
            return seats[offset + pivot] + 1


if __name__ == '__main__':
    with open("boarding_passes.txt", "r") as f:
        boarding_passes = f.read().splitlines()

    max_id = find_highest_seat_id(boarding_passes)

    print(f"The maximum seat ID was {max_id}")

    # not doing this earlier to show how I did it initially, although it would have been useful
    seat_ids = sorted([int(find_seat_id(seat)) for seat in boarding_passes])

    my_seat = find_seat(seat_ids)
    print(f"My seat number is {my_seat}")
