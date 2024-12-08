# AoC 2024, day 8

SAMPLE_FILE = "sample.txt"
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
    anitnode_locs = set()

    for row_idx, row in enumerate(day8_map):
        for col_idx, col in enumerate(day8_map[0]):
            if "." == day8_map[row_idx][col_idx]:
                continue
            else:
                antenna_loc = (row_idx, col_idx)
                antinode_set = calc_antinode_placement(day8_map, antenna_loc)
                anitnode_locs.update(antinode_set)

    return len(anitnode_locs)


def main():
    with open(DATA_FILE, "r") as file:
        day8_map = [list(line.strip()) for line in file]

    part_one_answer = part_one(day8_map)
    print(f"{part_one_answer = }")


if __name__ == "__main__":
    main()
