if __name__ == '__main__':
    with open("answers.txt", "r") as f:
        # quite proud of this PEP-8 compliant one liner
        # split the parties into groups, then make a set for each person in the group.
        # from this work out the union of those sets and calculate the length of it
        # after this has been done on every set, return a generator to the sum function, making a nice, memory efficient
        # one liner to do the job.
        total = sum(len(set.union(*[set(response) for response in group.split()])) for group in f.read().split("\n\n"))
    print(f"Part 1 total is {total}")

    with open("answers.txt", "r") as f:
        # this one is basically the same, I need to reread in the file to keep the above one liner so doing it again
        # sadly it doesn't all fit on one line without overrunning on character width, so compromising here
        total = sum(
            len(set.intersection(*[set(response) for response in group.split()])) for group in f.read().split("\n\n"))
    print(f"Part 2 total is {total}")
