#!/usr/bin/env python3

from collections import defaultdict
import numpy as np

def p1(instructions, map):
    # start with AAA
    element = 'AAA'
    end = 'ZZZ'
    step_count = 0
    found = False

    while not found:
        for ins in instructions:
            if 'R' == ins:
                element = map[element][1]
            else:
                element = map[element][0]

            step_count += 1
        
        if end == element:
            found = True
    
    return step_count
    
def p2(instructions, my_map):
    starters = [k for k in my_map.keys() if k[-1] == "A"]
    total_steps = [0] * len(starters)

    for idx, curr in enumerate(starters):
        while not curr.endswith("Z"):
            for i in instructions:
                total_steps[idx] += 1
                if 'R' == i:
                    curr = my_map[curr][1]
                else:
                    curr = my_map[curr][0]
            
    return np.lcm.reduce(total_steps)

def main():
    with open("input.txt", "r") as file:
        contents = file.read().split("\n")
    
    instructions = contents[0]

    # populate map
    map = defaultdict()
    for line in contents[2:]:
        line = line.split(" = ")
        values = ''.join(c for c in line[1] if c.isalpha() or c.isdigit())
        l, r = values[:3], values[3:]
        map[line[0]] = (l,r)
        
    p1_answer = p1(instructions, map)
    print(f"{p1_answer = }")

    p2_answer = p2(instructions, map)
    print(f"{p2_answer = }")


if __name__=="__main__":
    main()
