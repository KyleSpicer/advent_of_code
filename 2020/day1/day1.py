#!/usr/bin/env python3

def adds_to_2020(list_of_lines: list) -> int:
    print(list_of_lines)
    for i in list_of_lines:
        for j in list_of_lines:
            for k in list_of_lines:
                if i + j + k == 2020:
                    return i * j *k

def main():
    with open("input.txt") as file:
        lines = file.readlines()

    lines = [int(line.strip()) for line in lines]

    part_one = adds_to_2020(lines)
    print(f"{part_one = }")
    
if __name__=="__main__":
    main()