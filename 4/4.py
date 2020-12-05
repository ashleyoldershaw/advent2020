import re


def find_valid_passports_pt_1(entries):
    # we want to count up all the passports that have the following fields:
    """
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID) (optional, we won't look for this)
    """
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    count = 0
    for entry in entries:
        if required_fields.issubset(set(entry.keys())):
            count += 1

    return count


def find_valid_passports_pt_2(entries):
    # a lot of checks in here!
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    eye_colours = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    # regex are notorious for being difficult to understand, so here's explanations:
    #                         #
    #                          6 hex characters (a-f or 0-9)
    hcl_regex = re.compile(r'^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$')
    #                          9 numbers 0-9
    pid_regex = re.compile(r'^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$')

    count = 0
    for entry in entries:
        # check for each required value (a bit messy but split into logical chunks
        if required_fields.issubset(set(entry.keys())):
            # check birth year, issue year and expiration year
            if 1920 <= int(entry["byr"]) <= 2002 and 2010 <= int(entry["iyr"]) <= 2020 and \
                    2020 <= int(entry["eyr"]) <= 2030:
                # check height in acceptable range in either cm or in
                if (entry["hgt"][-2:] == "cm" and 150 <= int(entry["hgt"][:-2]) <= 193) or \
                        (entry["hgt"][-2:] == "in" and 59 <= int(entry["hgt"][:-2]) <= 76):
                    # finally check the regex and eye colours and increment
                    if hcl_regex.match(entry["hcl"]) and pid_regex.match(entry["pid"]) and entry["ecl"] in eye_colours:
                        count += 1

    return count


if __name__ == '__main__':
    with open("passports.txt", "r") as f:
        passports = [{pair.split(":")[0]: pair.split(":")[1] for pair in p.split()} for p in f.read().split("\n\n")]

    total_valid = find_valid_passports_pt_1(passports)
    print(f"The total number of valid passports for part 1 is {total_valid}")

    total_valid = find_valid_passports_pt_2(passports)
    print(f"The total number of valid passports for part 2 is {total_valid}")
