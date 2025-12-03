# AoC 2024, day 8

from re import S

SAMPLE_FILE = "sample.txt"
SAMPLE_2_FILE = "data2.txt"
DATA_FILE = "data.txt"


def display_map(curr_map):
    for line in curr_map:
        print(line)
    print()


def calc_antinode_placement(og_map, antenna_loc) -> set:
    """returns set of new antinode locations"""
    # generate blank map for recording antinodes
    antinode_map = [["." for _ in row] for row in og_map]

    new_antinode_set = set()
    same_freq_locs = set()

    ant_x, ant_y = antenna_loc
    curr_freq = og_map[ant_x][ant_y]
    antinode_map[ant_x][ant_y] = curr_freq

    # find same freq locations
    for row_i, row in enumerate(og_map):
        for col_i, col in enumerate(row):
            if row_i == ant_x and col_i == ant_y:
                continue  # skip processing freq
            if og_map[row_i][col_i] == curr_freq:
                same_freq_locs.add((row_i, col_i))

    # find difference and record anitnode loc
    for loc in same_freq_locs:
        curr_x, curr_y = loc
        diff_x = curr_x - ant_x
        diff_y = curr_y - ant_y
        new_diff_x = diff_x * 2
        new_diff_y = diff_y * 2
        new_anti_x = ant_x + new_diff_x
        new_anti_y = ant_y + new_diff_y

        if 0 <= new_anti_x < len(og_map) and 0 <= new_anti_y < len(og_map[0]):
            antinode_map[new_anti_x][new_anti_y] = "#"
            new_antinode_set.add((new_anti_x, new_anti_y))

    return new_antinode_set


def part_one(day8_map):
    antenna_locs = set()
    antinode_locs = set()

    for row_idx, row in enumerate(day8_map):
        for col_idx, col in enumerate(day8_map[0]):
            if "." == day8_map[row_idx][col_idx]:
                continue
            else:
                antenna_loc = (row_idx, col_idx)
                antinode_set = calc_antinode_placement(day8_map, antenna_loc)
                antinode_locs.update(antinode_set)

    return len(antinode_locs)


def part_two_populate_map(og_map, new_map, curr_loc):
    curr_x, curr_y = curr_loc
    curr_char = og_map[curr_x][curr_y]
    new_map[curr_x][curr_y] = curr_char
    same_freq_locs = set()
    new_antinode_set = set()

    for row_i, row in enumerate(og_map):
        for col_i, col in enumerate(og_map[0]):
            if row_i == curr_x and col_i == curr_y:
                continue  # skip current location
            if og_map[row_i][col_i] == curr_char:
                same_freq_locs.add((row_i, col_i))

    for loc in same_freq_locs:
        x, y = loc
        diff_x = x - curr_x
        diff_y = y - curr_y
        new_diff_x = diff_x * 2
        new_diff_y = diff_y * 2

        antinode_x = curr_x + new_diff_x
        antinode_y = curr_y + new_diff_y

        while 0 <= antinode_x < len(og_map) and 0 <= antinode_y < len(og_map[0]):
            new_map[antinode_x][antinode_y] = "#"
            antinode_x += new_diff_x
            antinode_y += new_diff_y

        antinode_x = curr_x - new_diff_x
        antinode_y = curr_y - new_diff_y
        while 0 <= antinode_x < len(og_map) and 0 <= antinode_y < len(og_map[0]):
            new_map[antinode_x][antinode_y] = "#"
            antinode_x -= new_diff_x
            antinode_y -= new_diff_y


def part_two(day8_map) -> int:
    antinode_locs = set()
    antenna_info = set()

    total_antinodes = 0

    antinode_map = [["." for _ in row] for row in day8_map]

    for row_idx, row in enumerate(day8_map):
        for col_idx, col in enumerate(day8_map[0]):
            if "." == day8_map[row_idx][col_idx]:
                continue
            else:
                antenna_loc = (row_idx, col_idx)
                part_two_populate_map(day8_map, antinode_map, antenna_loc)

    for row_idx, row in enumerate(day8_map):
        for col_idx, col in enumerate(day8_map[0]):
            if antinode_map[row_idx][col_idx] != ".":
                total_antinodes += 1

    return total_antinodes


def main():
    with open(DATA_FILE, "r") as file:
        day8_map = [list(line.strip()) for line in file]

    part_one_answer = part_one(day8_map)
    print(f"{part_one_answer = }")

    part_two_answer = part_two(day8_map)
    print(f"{part_two_answer = }")


if __name__ == "__main__":
    main()
