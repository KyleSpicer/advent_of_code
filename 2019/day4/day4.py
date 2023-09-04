#!/usr/bin/env python3

# Part One:
# it is a six digit number
# value is within range provided
# two adjacent digits are the same
# left to right, digits never decrease

# Part Two:
# dup numbers can only be two digits, never more


def check_decrease(num):
    num_str = str(num)
    for i in range(len(num_str) - 1):
        if int(num_str[i]) > int(num_str[i + 1]):
            return False
    return True


def check_adjacent_dup(num):
    num_str = (str(num))
    for i in range(len(num_str) - 1):
        if num_str[i] == num_str[i + 1]:
            return True
    return False


def check_adj_dup_p2(num):
    num_str = str(num)
    i = 0

    while i < len(num_str):
        digit_count = 1

        # Count consecutive occurrences of the current digit
        while i + 1 < len(num_str) and num_str[i] == num_str[i + 1]:
            digit_count += 1
            i += 1

        if digit_count == 2:
            return True

        i += 1


def part_one(data):
    start = data[0]
    end = data[1]

    compliant_passwords = 0

    for i in range(start, end + 1):
        if True == check_adjacent_dup(i):
            if True == check_decrease(i):
                compliant_passwords += 1

    return compliant_passwords


def part_two(data):
    start = data[0]
    end = data[1]
    compliant_passwords = 0

    for i in range(start, end + 1):
        if True == check_adj_dup_p2(i):
            if True == check_decrease(i):
                compliant_passwords += 1
    return compliant_passwords


def main():
    data = []
    with open("input.txt", "r") as file:
        lines = file.readline()
        data = [int(num) for num in lines.split("-")]

    p1 = part_one(data)
    print(f"Part One: {p1}")

    p2 = part_two(data)
    print(f"Part Two: {p2}")


if __name__ == "__main__":
    main()
