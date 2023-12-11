#!/usr/bin/env python3

directions = ['N', 'E', 'S', 'W']

def part_one(data):
    curr_dir = directions[0] # start facing north
    curr_x, curr_y = 0, 0
    visited = set()
    direction = ''
    dist = 0

    for ins in data:
        direction, dist = ins[0], int(ins[1:])

        if curr_dir == 'N' and direction == 'R':
            curr_dir = directions[1]
            curr_x += dist

        elif curr_dir == 'N' and direction == 'L':
            curr_dir = directions[-1]
            curr_x -= dist
                    
        elif curr_dir == 'E' and direction == 'R':
            curr_dir = directions[2]
            curr_x -= dist

        elif curr_dir == 'E' and direction == 'L':
            curr_dir = directions[0]
            curr_y += dist

        elif curr_dir == 'S' and direction == 'R':
            curr_dir = directions[-1]
            curr_x -= dist
        
        elif curr_dir == 'S' and direction == 'L':
            curr_dir = directions[1]
            curr_x += dist
        
        elif curr_dir == 'W' and direction == 'R':
            curr_dir = directions[0]
            curr_y += dist
        
        elif curr_dir == 'W' and direction == 'L':
            curr_dir = directions[2]
            curr_y -= dist
        

        coord = (curr_x, curr_y)
        if coord in visited:
            continue
        else:
            visited.add(coord)
            
        

    return abs(curr_x + curr_y)

def main():
    with open("input.txt") as file:
        data = file.read().split(', ')

    p1_answer = part_one(data)
    print(f"{p1_answer = }")

if __name__ == "__main__":
    main()


    # print()            
    # for item in visited:
    #     print(item)
    
    # # print(f"part 1: {abs(current_x + current_y)} blocks away from start")
    # print(f"\npart 2: {abs(current_x + current_y)} blocks away from start\n")
    