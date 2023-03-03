#!/usr/bin/env python3

from math import sqrt

def get_neighbors(input, x, y, first_dictionary):
    sum = 0
    for k,v in first_dictionary.items():
        if abs(k[0] - x) < 2 and abs(k[1] - y) < 2:
            sum += v

    return sum
    

def display_grid_and_num(input):
    all_points = {}
    x = 0
    y = 0
    part1 = 0
    part2 = 0
    directions = ['W', 'S', 'E', 'N']
    dir_idx = 2
    current_direction = directions[dir_idx] # starting east
    steps = 1 # up to 2
    advance = 1 # number of steps to advance per direction
    iters = 2
    all_points[0,0] = 1

    while iters < input and not part1:
        for _ in range(advance):
            if current_direction == 'E':
                x += 1
            elif current_direction == 'N':
                y += 1
            elif current_direction == 'W':
                x -= 1
            else: 
                y -= 1

            if not part2:
                new_number = get_neighbors(iters, x, y, all_points)            
                all_points[x,y] = new_number 

            if new_number > input and not part2:
                part2 = new_number
            
            if iters == input:
                part1 = abs(x + y)    
            iters += 1

        current_direction = directions[(dir_idx + 1) % 4]
        steps = (steps + 1) % 2
        dir_idx += 1
        if steps == 1:
            advance += 1

    return part1, part2

def main():
    input = 361527
    part1, part2 = display_grid_and_num(input)
    print(f"part one: {part1}")
    print(f"part two: {part2}")

if __name__=="__main__":
    main()