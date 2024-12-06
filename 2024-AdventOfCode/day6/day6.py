# AoC 2024, day 6

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


def part_two(guard_map):
    pass


def main():
    with open(SAMPLE_FILE, "r") as file:
        guard_map = [list(line.strip()) for line in file]

    part_one_answer = part_one(deepcopy(guard_map))
    print(f"{part_one_answer = }")

    part_two_answer = part_two(deepcopy(guard_map))
    print(f"{part_two_answer = }")


if __name__ == "__main__":
    main()
