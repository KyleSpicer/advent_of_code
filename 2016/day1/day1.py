#!/usr/bin/env python3

# def add_each_block_visited()

def main():
    with open("sample.txt") as file:
        line = file.readline()
        line = line.split(", ")
    
    # begin facing north
    previous_x = 0
    previous_y = 0
    
    # keep track of location
    current_x = 0
    current_y = 0
    
    # current facing position
    possible_directions = ['N', 'E', 'S', 'W']
    current_direction = possible_directions[0]
    
    direction = ''
    distance = 0
    
    visited = []
    
    for instruction in line:
        direction = instruction[0]
        distance = int(instruction[1:])
        print("new_coord: ", end="")
        print(current_x, current_y)
        
        if current_direction == 'N' and direction == 'R':
            # go east, increase current x
            current_direction = possible_directions[1]
            current_x += distance
            coord = (current_x, current_y)
            if coord in visited:
                break
            else:
                visited.append(coord)
            
        elif current_direction == 'N' and direction == 'L':
            # facing west, decrease current x
            current_direction = possible_directions[-1]
            current_x -= distance
            coord = (current_x, current_y)
            if coord in visited:
                break
            else:
                visited.append(coord)
        
        elif current_direction == 'E' and direction == 'R':
            # facing south, decrease y
            current_direction = possible_directions[2]
            current_y -= distance
            coord = (current_x, current_y)
            if coord in visited:
                break
            else:
                visited.append(coord)
        
        elif current_direction == 'E' and direction == 'L':
            # facing north, increase y
            current_direction = possible_directions[0]
            current_y += distance
            coord = (current_x, current_y)
            if coord in visited:
                break
            else:
                visited.append(coord)
            
        elif current_direction == 'S' and direction == 'R':
            # facing west, decrease current x
            current_direction = possible_directions[-1]
            current_x -= distance
            coord = (current_x, current_y)
            if coord in visited:
                break
            else:
                visited.append(coord)

        
        elif current_direction == 'S' and direction == 'L':
            # facing east, increase x
            current_direction = possible_directions[1]
            current_x += distance
            coord = (current_x, current_y)
            if coord in visited:
                break
            else:
                visited.append(coord)

            
        elif current_direction == 'W' and direction == 'R':
            # facing north, increase y
            current_direction = possible_directions[0]
            current_y += distance
            coord = (current_x, current_y)
            if coord in visited:
                break
            else:
                visited.append(coord)

            
        elif current_direction == 'W' and direction == 'L':
            # facing south, decrease y
            current_direction = possible_directions[2]
            current_y -= distance
            coord = (current_x, current_y)
            if coord in visited:
                break
            else:
                visited.append(coord)
    
    print()            
    for item in visited:
        print(item)
    
    # print(f"part 1: {abs(current_x + current_y)} blocks away from start")
    print(f"\npart 2: {abs(current_x + current_y)} blocks away from start\n")
    

if __name__ == "__main__":
    main()