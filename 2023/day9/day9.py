#!/usr/bin/env python3

from itertools import tee
from copy import deepcopy as dc

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def process_line(line):
    all_lists = []
    all_lists.append(line) # add starting sequence

    # populate all sub lists until only 0's are present
    while True:
        if all(x == 0 for x in line):
               break
        
        line = [y - x for x, y in pairwise(line)]
        all_lists.append(line)
    
    all_lists = list(reversed(all_lists))
    for i, l in enumerate(all_lists):
        try:
            all_lists[i + 1].append(l[-1] + all_lists[i + 1][-1])

        except IndexError:
            pass
    
    return all_lists[-1][-1]

def process_p1(contents):
    next_values = []

    for line in contents:
        next_values.append(process_line(line))

    return sum(next_values)

def process_line_p2(line):
    all_lists = []
    all_lists.append(list(reversed(line)))

    while True:
        if all(x == 0 for x in line):
               break
        line = [y - x for x, y in pairwise(line)]
        all_lists.append(list(reversed(line)))
    
    all_lists = list(reversed(all_lists))

    for i, l in enumerate(all_lists):
        try:
            all_lists[i + 1].append(all_lists[i + 1][-1] - l[-1])
        
        except IndexError:
            pass
            
    return all_lists[-1][-1]

def process_p2(contents):
    next_values = []

    for line in contents:
        next_values.append(process_line_p2(line))
    
    return sum(next_values)

def main():
    with open("input.txt", "r") as file:
        contents = file.readlines()
        
    nums = []
    for line in contents:
        nums.append(list(map(int, line.split())))

    p1_answer = process_p1(dc(nums))
    print(f"{p1_answer = }")

    p2_answer = process_p2(dc(nums))
    print(f"{p2_answer = }")


if __name__=="__main__":
    main()
