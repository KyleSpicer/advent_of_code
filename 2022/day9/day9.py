#!/usr/bin/env python3

from copy import deepcopy            
from typing import Tuple

def find_w_h(data) -> Tuple[int, int]:
    curr_x = 0
    curr_y = 0

    min_x = 0
    min_y = 0

    max_x = -10000
    max_y = -10000

    for line in data:
        if line[0] == 'R':
            curr_x += line[1]
            if curr_x > max_x:
                max_x = curr_x

        elif line[0] == 'L':
            curr_x -= line[1]
            if curr_x < min_x:
                min_x = curr_x

        elif line[0] == 'U':
            curr_y += line[1]
            if curr_y > max_y:
                max_y = curr_y

        elif line[0] == 'D':
            curr_y -= line[1]
            if curr_y < min_y:
                min_y = curr_y

    ret_x = abs((max_x - min_x) + 1)
    ret_y = abs((max_y - min_y) + 1)

    return ret_x, ret_y

def create_grid(x, y):
    return [['.' for _ in range(y)] for _ in range(x)]

def display_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()

def part_one(data) -> int:
    total_t_positions = 0
    max_width, max_height = find_w_h(data)
    
    grid = create_grid(max_width, max_height)
    
    print("== Initial State ==\n")
    grid[max_height][0] = 'H' # place starting head in position
    display_grid(grid)

    curr_x = 0
    curr_y = max_height
    instruction_count = 0

    for instruction in data:
        dir = instruction[0]
        count = instruction[1]

        # if dir == "R":
        #     for x in range(count):
        #         grid[curr_y][curr_x] = "H"
        #         grid[curr_y][curr_x - 1] = "."
        #         curr_x += 1
        
        # if dir == "L":
        #     for x in range(count):
        #         grid[curr_y][curr_x] = "H"
        #         grid[curr_y][curr_x + 1] = "."
        #         curr_x -= 1
        
        # if dir == "U":
        #     for x in range(count):
        #         grid[curr_y][curr_x] = "H"
        #         grid[curr_y - 1][curr_x] = '.'
        #         curr_y += 1

        # if dir == "D":
        #     for x in range(count):
        #         grid[curr_y][curr_x] = "H"
        #         grid[curr_y + 1][curr_x] = '.'
        #         curr_y -= 1

        print(f"== {instruction} ==")
        display_grid(grid)

        instruction_count += 1

    return total_t_positions

def main():
    with open("sample.txt", "r") as file:
        data = file.readlines()
        data = [line.strip().split(" ") for line in data]
        data = [[line[0], int(line[1])] for line in data]

    p1 = part_one(deepcopy(data))
    print(f"Part One: {p1}")
    

if __name__=="__main__":
    main()
