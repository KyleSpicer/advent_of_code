#!/usr/bin/env python3

from collections import defaultdict
import numpy as np

def ring_bell():
    print('\a')

def calc_answer(pairs_list, galaxies_coord_dict):
    sum_paths = 0

    for pair in pairs_list:
        start_coord = galaxies_coord_dict[pair[0]]
        end_coord = galaxies_coord_dict[pair[1]]

        result = manhattan_dist(start_coord, end_coord)
        sum_paths += result

    return sum_paths
        
def manhattan_dist(start_coord, end_coord):
    x1, x2 = start_coord
    y1, y2 = end_coord
    loc1 = np.array([x1, x2])
    loc2 = np.array([y1, y2])
    m_dist = np.sum(np.abs(loc1 - loc2))
    return m_dist

def gen_galaxies_coordinates(grid):
    coord_dict = defaultdict()

    galaxy = 1

    for row_num, row in enumerate(grid):
        for col_num, col in enumerate(grid[0]):
            if grid[row_num][col_num] == '#':
                coord_dict[galaxy] = (row_num, col_num)
                galaxy += 1
    
    return coord_dict

def gen_pairs_list(num_galaxies):
    pairs = []

    for i in range(1, num_galaxies + 1):
        for j in range(1, num_galaxies + 1):
            if i == j:
                continue
            else:
                if (j, i) in pairs:
                    continue
                else:
                    pairs.append((i, j))

    return pairs

def gen_empty_cols_list(data):
    empty_cols_list = []

    for col_num in range(len(data[0])):
        col = [row[col_num] for row in data]
        if all(char == col[0] for char in col):
            empty_cols_list.append(col_num)

    return empty_cols_list

def gen_empty_rows_list(data):
    empty_rows_list = []

    for row_num, row in enumerate(data):
        if all(char == row[0] for char in row):
            empty_rows_list.append(row_num)

    return empty_rows_list

def expand_universe(galaxy_coords, expansion_amount, empty_rows, empty_cols):

    # expand columns
    for k, v in galaxy_coords.items():
        expand_count = 0
        for empty_col in empty_cols:
            if v[1] > empty_col:
                expand_count += 1
        galaxy_coords[k] = (v[0], v[1] + ((expand_count + expansion_amount) * expansion_amount))    

    # expand rows
    for k, v in galaxy_coords.items():
        expand_count = 0
        for empty_row in empty_rows:
            if v[0] > empty_row:
                expand_count += 1
        galaxy_coords[k] = (v[0] + ((expand_count + expansion_amount) * expansion_amount), v[1])

def main():
    with open("input.txt", "r") as file:
        data = file.readlines()
        data = [list(line.strip()) for line in data]

    expansion_size = 999999

    # find empty rows / columns
    empty_rows_list = gen_empty_rows_list(data)
    empty_cols_list = gen_empty_cols_list(data)
    
    # get coordinates of each point
    galaxies_coordinates = gen_galaxies_coordinates(data)

    # expand universe / grid coordinates
    expand_universe(galaxies_coordinates, expansion_size, empty_rows_list, empty_cols_list)

    answer = calc_answer(gen_pairs_list(len(galaxies_coordinates)), galaxies_coordinates)
    
    print(f"{answer = }")

    ring_bell()

if __name__=="__main__":
    main()