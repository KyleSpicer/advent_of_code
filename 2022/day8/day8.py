#!/usr/bin/env python3

from copy import deepcopy

def print_grid(grid):
    for row in grid:
        for num in row:
            print(num, end='')
        print()

def find_neighbors(grid, x, y) -> list:
    neighbors = []
    rows = len(grid)
    cols = len(grid[0])
    
    # check left neighbor
    if x > 0:
        neighbors.append(grid[x-1][y])
    
    # check top neighbor
    if y > 0:
        neighbors.append(grid[x][y - 1])
    
    # check right neighbor
    if x < rows - 1:
        neighbors.append(grid[x + 1][y])
    
    # check left neighbor
    if y < cols - 1: 
        neighbors.append(grid[x][y + 1])
    
    return neighbors

def surrounding_tree_count(grid) -> int:
    rows = len(grid)
    cols = len(grid[0])

    total_surrounding = 0

    # top and bottom rows count
    total_surrounding += rows * 2
    
    # left and right col count, minus 4 corners
    total_surrounding += (cols * 2) - 4

    return total_surrounding

def is_visible(grid, x, y):
    rows = len(grid)
    cols = len(grid[0])

    vis_up = True
    vis_down = True
    vis_left = True
    vis_right = True

    curr = grid[y][x]

    # check right
    for num in range(x + 1, rows, 1):
        if grid[y][num] >= curr:
            vis_right = False
            break
    # check left
    for num in range(x - 1, -1, -1):
        if grid[y][num] >= curr:
            vis_left = False
            break

    # check up
    for num in range(y - 1, -1, -1):
        if grid[num][x] >= curr:
            vis_up = False
            break

    # # check down
    for num in range(y + 1, cols, 1):
        if grid[num][x] >= curr:
            vis_down = False
            break

    
    return any([vis_up, vis_down, vis_right, vis_left])
         
def part_one(grid) -> int:
    visible_count = 0
    rows = len(grid)
    cols = len(grid[0])

    # count surrounding trees
    visible_count += surrounding_tree_count(grid)

    # check trees of interior grid
    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            curr = grid[x][y]
            visible = is_visible(grid, x, y)
            if visible:
                visible_count += 1

    return visible_count

def part_two(grid) -> int:

    return 0

def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    data = []
    for line in lines:
        curr_line = []
        row_data = line.strip().split()
        for num in row_data:
            for digit in num:
                curr_line.append(int(digit))

        data.append(curr_line)
        
    
    p1 = part_one(deepcopy(data))
    print(f"Part one: {p1}")

    p2 = part_two(deepcopy(data))
    print(f"Part two: {p2}")


if __name__=="__main__":
    main()
