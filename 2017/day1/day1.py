#!/usr/bin/env python3

def string_to_list(line: str) -> list:
    arr = []
    for letter in line:
        if letter == '\n':
            continue
        arr.append(int(letter))
    return arr

def sum_matching_digits(array: list) -> int:
    sum = 0
    previous = array[0]
    for idx in range(1, len(array)):
        if array[idx] == previous:
            sum += array[idx]
        previous = array[idx]
    
    if array[0] == array[-1]:
        sum += array[0]

    print(sum)
    return sum

def halfway_calculation(line: list) -> int:
    result = 0
    # print(line)
    steps_ahead = int(len(line) / 2)
    for idx in range(0, len(line)):
        # print(f"{line[idx] = }")
        # print(f"{line[(idx + steps_ahead) % len(line)] = }")
        if line[idx] == line[(idx + steps_ahead) % len(line)]:
            result += line[idx]
    
    return result
        




def main():
    with open("input.txt") as file:
        lines = file.readlines()
    
    for line in lines:
        print(line, end='')
    print("\n")

    # sum of all digits that match the next digit in the list
    # The list is circular, so the digit after the last digit is the first digit in the list.

    # PART 1:
    # for line in lines:
    #     line = string_to_list(line) # converts string to list of integers
    #     result = sum_matching_digits(line)
    #     print(f"part 1: {result}")
        
    # PART 2:
    for line in lines:
        line = string_to_list(line)
        result = halfway_calculation(line)
        print(result)

if __name__=="__main__":
    main()