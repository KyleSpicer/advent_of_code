#!/usr/bin/env python3

def convert_string_to_list_of_ints(line: str) -> list:
    line_list = line.split("\t")
    new_list = []
    for number in line_list:
        number = number.strip()
        new_list.append(int(number))

    return new_list

def part_two(line: list) -> int:
    sum = 0
    for idx in range(0, len(line)):
        for sidx in range(0, len(line)):
            if idx == sidx:
                continue
            else:
                if line[idx] % line[sidx] == 0:
                    sum += (line[idx] / line[sidx])

    return sum


def main():
    with open("input.txt") as file:
        row = file.readlines()
    
    checksum = 0
    
    # for line in row:
    #     new_line = convert_string_to_list_of_ints(line)
    #     new_line.sort()
    #     print(new_line)
    #     checksum += (new_line[-1] - new_line[0])

    # print(f"part 1: {checksum}")

    for line in row:
        new_line = convert_string_to_list_of_ints(line)
        new_line.sort()
        checksum += part_two(new_line)

    print(f"part 2: {round(checksum)}")

if __name__=="__main__":
    main()