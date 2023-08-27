#!/usr/bin/env python3.8

def part_one(data):
    number_of_increases = 0
    previous_depth = data[0]

    for depth in data:
        if depth > previous_depth:
            number_of_increases += 1
        previous_depth = depth
    
    return number_of_increases

def part_two(data):
    measurement_windows = []

    for curr_idx in range(len(data) - 2):
        first = data[curr_idx]
        second = data[curr_idx + 1]
        third = data[curr_idx + 2]
        sum = first + second + third
        measurement_windows.append(sum)
    
    return part_one(measurement_windows)
    

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines = [int(line) for line in lines]
    
    part_one_answer = part_one(lines)
    print(f"Part One: {part_one_answer}")

    part_two_answer = part_two(lines)
    print(f"Part Two: {part_two_answer}")

    

if __name__=="__main__":
    main()
