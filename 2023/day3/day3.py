#!/usr/bin/env python3

def print_grid(grid):
    for row in grid:
        print(row)

def process_special_char(grid, r, c, found_nums):
    connected_nums = []
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),            (0, 1),
        (1, -1),   (1, 0),  (1, 1)
    ]

    try:
        for dr, dc in directions:
            curr_r, curr_c = r + dr, c + dc
            if 0 > curr_r or curr_c >= len(grid[0]):
                pass

            else:
                num_str = ""
                curr_val = grid[curr_r][curr_c]

                if curr_val.isdigit():
                    num_str = f"{curr_val}"

                    # look left for additional numbers
                    temp_c = curr_c
                    while temp_c - 1 > -1 and grid[curr_r][temp_c - 1].isdigit():
                        temp_c -= 1
                        num_str = f"{grid[curr_r][temp_c]}{num_str}"

                    # look right for additional numbers
                    temp_c = curr_c
                    while temp_c + 1 < len(grid[0]) and grid[curr_r][temp_c + 1].isdigit():
                        temp_c += 1
                        num_str = f"{num_str}{grid[curr_r][temp_c]}"
                
                    if [curr_r, temp_c] not in found_nums:
                        found_nums.append([curr_r, temp_c])
                        connected_nums.append(int(num_str))
                    num_str = ""

    except IndexError:
        pass

    return connected_nums

def p1(grid):
    total_nums = []
    found_nums = []

    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            if col != '.' and not col.isdigit():
                num_list = process_special_char(grid, row_idx, col_idx, found_nums)
                try:
                    for num in num_list:
                            total_nums.append(num)
                except TypeError:
                    pass

    return sum(total_nums)

def p2(grid):
    gear_ratios = []
    found_nums = []

    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            if col != '.' and not col.isdigit():
                num_list = process_special_char(grid, row_idx, col_idx, found_nums)
                try:
                    if 2 == len(num_list):
                        gear_ratios.append(int(num_list[0]) * int(num_list[1]))

                except TypeError:
                    pass

    return sum(gear_ratios)

def main():
    with open("input.txt", "r") as file:
        contents = file.readlines()
        contents = [line.strip() for line in contents]

    grid = [list(line.strip()) for line in contents]

    p1_answer = p1(grid)
    print(f"{p1_answer = }")
    
    p2_answer = p2(grid)
    print(f"{p2_answer = }")

if __name__=="__main__":
    main()