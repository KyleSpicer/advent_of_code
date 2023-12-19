#!/usr/bin/env python3

from sys import argv
from collections import defaultdict

directions = {
    '|':[(-1,0), (1,0)],    # connecting north and south
    '-':[(0,-1), (0,1)],    # connecting east and west
    'L':[(-1,0), (0,1)],    # connecting north and east
    'J':[(-1,0), (0,-1)],   # connecting north and west
    '7':[(1,0), (0,-1)],    # connecting south and west
    'F':[(1,0), (0,1)],     # connecting south and east
    'S':[(-1,0),(0,-1),(0,1),(1,0)],  # starting position
    '.':[],                 # ground
}

def find_start_pos(board):
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            val = board[r][c]
            if val == 'S':
                return r, c

def find_neighbors(grid, row, col):
    neighbors = []

    try:
        valid_neighbors = directions[grid[row][col]]
    except IndexError:
        return neighbors

    for n in valid_neighbors:
        nr, nc = n
        neighbors.append((nr + row, nc + col))
    
    return neighbors

def bfs(grid, start_r, start_c):
    visited = set()
    distances = defaultdict()

    # add start pos to queue with distance of 0
    queue = [[(start_r, start_c), 0]]

    while queue:
        coord, distance = queue.pop()
        if coord in visited:
            continue
        
        visited.add(coord)
        distances[coord] = distance

        if (neighbors := find_neighbors(grid, *coord)):
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                queue.append((neighbor, distance + 1))

    p1_answer = (max(distances.values()) // 2) + 1
    print(f"{p1_answer = }")

    return visited

def count_crossings(grid_row, visited, r, c):
    count = 0

    for point in range(c):
        # incrementing across row and counting the barriers crossed
        if (r, point) not in visited:
            continue
        
        count += grid_row[point] in ['J', 'L', '|', 'S']

    return count

def part_two(grid, visited):
    total_enclosed = 0

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            curr_coord = (r, c)
            
            if curr_coord in visited:
                continue
            
            crossings = count_crossings(grid[r], visited, *curr_coord)

            if crossings % 2 != 0:
                total_enclosed += 1

    return total_enclosed
    
def main():
    if 2 != len(argv):
        print(f"Usage: {argv[0]} <filename>")
        return
    
    with open(argv[1], "r") as file:
        data = [list(line.strip()) for line in file.readlines()]

    # get starting position
    start_coord = find_start_pos(data)

    visited = bfs(data, *start_coord)

    # Need to complete part two
    p2_answer = part_two(data, visited)
    print(f"{p2_answer = }")

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
