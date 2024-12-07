# AoC 2024, day 6

import time
from copy import deepcopy

SAMPLE_FILE = "sample.txt"
DATA_FILE = "data.txt"

directions = [
    (-1, 0),  # north
    (0, 1),  # east
    (1, 0),  # south
    (0, -1),  # west
]


def display_map(curr_map):
    for row in curr_map:
        print(row)


def get_start_pos(guard_map):
    # find guard position
    start_pos = ()
    for row_i, row in enumerate(guard_map):
        for col_i, col in enumerate(row):
            if col == "^":
                start_pos = (row_i, col_i)
        if start_pos:
            break
    return start_pos


def part_one(guard_map):
    curr_pos = get_start_pos(guard_map)
    curr_dir = directions[0]  # start facing north
    curr_dir_idx = 0
    visited_positions = set()

    while True:
        from time import sleep

        display_map(guard_map)
        sleep(0.5)
        print()
        visited_positions.add(curr_pos)
        curr_dir = directions[curr_dir_idx]
        next_pos = (curr_pos[0] + curr_dir[0], curr_pos[1] + curr_dir[1])

        if 0 <= next_pos[0] < len(guard_map) and 0 <= next_pos[1] < len(guard_map[0]):
            next_pos_char = guard_map[next_pos[0]][next_pos[1]]

            if next_pos_char == "#":
                # rotate 90 degrees
                curr_dir_idx = (curr_dir_idx + 1) % len(directions)

            else:
                guard_map[curr_pos[0]][curr_pos[1]] = "X"
                curr_pos = next_pos
                guard_map[curr_pos[0]][curr_pos[1]] = "*"

        else:
            guard_map[curr_pos[0]][curr_pos[1]] = "X"
            break

    return len(visited_positions)


def produces_infinite_loop(guard_map) -> bool:
    curr_pos = get_start_pos(guard_map)
    curr_dir = directions[0]  # start facing north
    curr_dir_idx = 0
    visited_positions = set()

    while True:
        curr_dir = directions[curr_dir_idx]
        if (curr_pos, curr_dir) in visited_positions:
            return True
        visited_positions.add((curr_pos, curr_dir))
        next_pos = (curr_pos[0] + curr_dir[0], curr_pos[1] + curr_dir[1])

        if 0 <= next_pos[0] < len(guard_map) and 0 <= next_pos[1] < len(guard_map[0]):
            next_pos_char = guard_map[next_pos[0]][next_pos[1]]

            if next_pos_char in ["#", "0"]:
                # rotate 90 degrees
                curr_dir_idx = (curr_dir_idx + 1) % len(directions)

            else:
                guard_map[curr_pos[0]][curr_pos[1]] = "X"
                curr_pos = next_pos
                guard_map[curr_pos[0]][curr_pos[1]] = "*"

        else:
            guard_map[curr_pos[0]][curr_pos[1]] = "X"
            break

    return False


def part_two(guard_map):
    loop_count = 0

    for row in range(len(guard_map)):
        for col in range(len(guard_map[0])):
            if guard_map[row][col] in ["#", "^"]:
                continue
            new_map = deepcopy(guard_map)
            new_map[row][col] = "0"  # add obstacle
            if produces_infinite_loop(new_map):
                loop_count += 1
    return loop_count


def main():
    start_time = time.time()

    with open(SAMPLE_FILE, "r") as file:
        guard_map = [list(line.strip()) for line in file]

    part_one_answer = part_one(deepcopy(guard_map))
    print(f"{part_one_answer = }")

    part_two_answer = part_two(deepcopy(guard_map))
    print(f"{part_two_answer = }")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting day 6...")
