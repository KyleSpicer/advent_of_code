#!/usr/bin/env python3

from sys import argv
from copy import deepcopy as dc

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end='')
        print()

def tilt_north(grid):
    g = grid
    for i, row in enumerate(g):
        if not any(char == 'O' for char in row):
            continue
        for j, col in enumerate(row):
            if g[i][j] == 'O':
                curr_x = i
                while curr_x > 0 and grid[curr_x - 1][j] not in ['#', 'O']:
                    curr_x -= 1
                g[i][j] = '.'
                g[curr_x][j] = 'O'

    return g

def tilt_south(grid):
    g = grid
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        if not any(char == 'O' for char in row):
            continue

        for j, char in enumerate(row):
            if grid[i][j] == 'O':
                curr_x = i
                while curr_x < len(grid) - 1 and grid[curr_x + 1][j] not in ['#', 'O']:
                    curr_x += 1
                g[i][j] = '.'
                g[curr_x][j] = 'O'
    return g

def tilt_west(grid):
    g = grid
    for i, row in enumerate(g):
        if not any(char == 'O' for char in row):
            continue
        for j, col in enumerate(row):
            if g[i][j] == 'O':
                curr_y = j
                while curr_y > 0 and grid[i][curr_y - 1] not in ['#', 'O']:
                    curr_y -= 1

                g[i][j] = '.'
                g[i][curr_y] = 'O'
    return g

def tilt_east(grid):
    g = grid
    for i, row in enumerate(grid):
        if not any(char == 'O' for char in row):
            continue
        for j in range(len(row) -1, -1, -1):
            if g[i][j] == 'O':
                curr_y = j
                while curr_y < len(row) - 1 and grid[i][curr_y + 1] not in ['#', 'O']:
                    curr_y += 1
                
                g[i][j] = '.'
                g[i][curr_y] = 'O'
    return g

def spin_cycle(grid):
    # north, west, south, east
    n = tilt_north(grid)
    w = tilt_west(n)
    s = tilt_south(w)
    e = tilt_east(s)

    return e

def calc_total_load(grid):
    length = len(grid)
    curr_row = 0
    total = 0

    for x in range(length, 0, -1):
        row = grid[curr_row]
        count = row.count('O')
        total += x * count
        curr_row += 1

    return total 

def part_one(data):
    grid = dc(data)
    tilted_north = tilt_north(grid)
    p1_answer = calc_total_load(tilted_north)
    print(f"{p1_answer = }")

def get_hash(grid):
    return "\n".join(["".join(line) for line in grid])

def part_two(data):
    # efficient solution help from: https://github.com/womogenes/AoC-2023-Solutions/blob/main/day_14/day_14_p2.py

    spin_cycle_amount = 1000000000

    cycle_to_grid = {}
    seen = {}

    for i in range(spin_cycle_amount):
        data = spin_cycle(data)
        hash = get_hash(data)
        if hash in seen:
            period = i - seen[hash]
            billionth_grid = cycle_to_grid[(spin_cycle_amount - 1 - seen[hash]) % period + seen[hash]]
            p2_answer = calc_total_load(billionth_grid)
            print(f"{p2_answer = }")
            break
            

        seen[get_hash(data)] = i
        cycle_to_grid[i] = dc(data)

def main():
    if 2 != len(argv):
        print(f"Usage: {argv[0]} <filename>")
        return
    
    with open(argv[1], "r") as file:
        data = [list(line.strip()) for line in file.readlines()]

    part_one(data)
    part_two(dc(data))


if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
