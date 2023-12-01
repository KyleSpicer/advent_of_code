#!/usr/bin/env python3

# part one uses sample.txt
# part two uses sample2.txt
# both use input.txt

from copy import deepcopy

nums = {
    "one": 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
    }


def p1(data):
    p1_sum = 0

    for line in data:
        value = p1_get_value(line)
        p1_sum += value

    return p1_sum

def p1_get_value(line):
    value_str = ""

    # forward traversal to find first number
    for letter in line:
        if letter.isdigit():
            value_str = letter
            break

    # reverse traversal to find last number
    for letter in line[::-1]:
        if letter.isdigit():
            value_str = f"{value_str}{letter}"
            break

    return int(value_str)

def p2(data):
    p2_sum = 0

    for line in data:
        value = p2_get_value(line)
        p2_sum += value

    return p2_sum

def p2_get_value(line):
    val_str = ""

    forward_num = forward_val(line)
    reverse_num = reverse_val(line)

    val_str = f"{forward_num}{reverse_num}"

    return int(val_str)

def forward_val(line):
    f = line
    for _ in range(len(f)):
        if f[0].isdigit():
            return f[0]
        
        else:
            for k,v in nums.items():
                if k == f[:len(k)]:
                    return str(v)
                
            f = f[1:]
    
def reverse_val(line):
    r = line

    for _ in range(len(r)):
        if r[-1].isdigit():
            return r[-1]
        
        else:
            for k,v in nums.items():
                if k == r[-len(k):]:
                    return str(v)
            
            r = r[:-1]

def main():
    with open("input.txt", "r") as file:
        contents = file.readlines()
        contents = [line.strip() for line in contents]
    
    p1_solution = p1(contents)
    print(f"{p1_solution = }")
    
    p2_solution = p2(deepcopy(contents))
    print(f"{p2_solution = }")

if __name__== "__main__":
    main()