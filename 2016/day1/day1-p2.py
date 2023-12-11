#!/usr/bin/env python3

directions = ['N', 'E', 'S', 'W']
factors = (
    (0, 1),   # N
    (1, 0),   # E
    (0, -1),  # S
    (-1, 0)   # W
)

def part_two(data):
    curr_dir = directions[0] # start facing north
    curr_x, curr_y = 0, 0
    prev_x, prev_y = 0, 0
    visited = set()
    direction = ''
    dist = 0

    for ins in data:
        prev_x, prev_y = curr_x, curr_y
        direction, dist = ins[0], int(ins[1:])

        if curr_dir == 'N' and direction == 'R':
            curr_dir = directions[1]
            curr_y += dist

        elif curr_dir == 'N' and direction == 'L':
            curr_dir = directions[-1]
            curr_y -= dist
                    
        elif curr_dir == 'E' and direction == 'R':
            curr_dir = directions[2]
            curr_x += dist

        elif curr_dir == 'E' and direction == 'L':
            curr_dir = directions[0]
            curr_x -= dist

        elif curr_dir == 'S' and direction == 'R':
            curr_dir = directions[-1]
            curr_y -= dist
        
        elif curr_dir == 'S' and direction == 'L':
            curr_dir = directions[1]
            curr_y += dist
        
        elif curr_dir == 'W' and direction == 'R':
            curr_dir = directions[0]
            curr_x -= dist
        
        elif curr_dir == 'W' and direction == 'L':
            curr_dir = directions[2]
            curr_x += dist
        

        start_x = prev_x
        start_y = prev_y
        end_x = curr_x
        end_y = curr_y

        if curr_dir == 'N':
            # decrement x
            for i in range(start_x, end_x, -1):
                coord = (i, end_y)
                if coord in visited:
                    print(f"{coord = }")
                    return abs(coord[0]) + abs(coord[1])
                
                visited.add(coord)

        if curr_dir == 'E':
            # increment y
            for i in range(start_y, end_y, 1):
                coord = (end_x, i)
                if coord in visited:
                    print(f"{coord = }")
                    return abs(coord[0]) + abs(coord[1])
                visited.add(coord)
            
        if curr_dir == 'S':
            # increment x
            for i in range(start_x, end_x, 1):
                coord = (i, end_y)
                if coord in visited:
                    print(f"{coord = }")
                    return abs(coord[0]) + abs(coord[1])
                visited.add(coord)
            
        if curr_dir == 'W':
            # decrement y
            for i in range(start_y, end_y, -1):
                coord = (end_x, i)
                if coord in visited:
                    print(f"{coord = }")
                    return abs(coord[0]) + abs(coord[1])
                visited.add(coord)
        
    return 0

def main():
    with open("input.txt") as file:
        data = file.read().split(', ')

    p2_answer = part_two(data)
    print(f"{p2_answer = }")

if __name__ == "__main__":
    main()