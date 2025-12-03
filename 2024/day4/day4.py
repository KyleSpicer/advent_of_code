# AoC 2024, day 4

from re import A, M, S

SAMPLE_FILE = "sample.txt"
DATA_FILE = "data.txt"

directions = [
    (-1, 0),  # up
    (-1, 1),  # up and right
    (0, 1),  # right
    (1, 1),  # right and down
    (1, 0),  # down
    (1, -1),  # down and left
    (0, -1),  # left
    (-1, -1),  # up and left
]


def part_one(xmas_map):
    xmas_count = 0

    for row in range(len(xmas_map)):
        for col in range(len(xmas_map[0])):
            if xmas_map[row][col] != "X":
                continue  # skip it

            for dr, dc in directions:
                # do bound checking
                new_row = row + 3 * dr
                new_col = col + 3 * dc

                if new_row < 0 or new_row >= len(xmas_map):
                    continue
                if new_col < 0 or new_col >= len(xmas_map[0]):
                    continue

                # process X
                if xmas_map[row + dr][col + dc] == "M":
                    if xmas_map[row + 2 * dr][col + 2 * dc] == "A":
                        if xmas_map[row + 3 * dr][col + 3 * dc] == "S":
                            xmas_count += 1

    return xmas_count


def part_two(xmas_map):
    count = 0

    for row in range(1, len(xmas_map) - 1):
        for col in range(1, len(xmas_map[0]) - 1):
            if xmas_map[row][col] != "A":
                continue

            corners = [
                xmas_map[row - 1][col - 1],  # up and left
                xmas_map[row - 1][col + 1],  # up and right
                xmas_map[row + 1][col + 1],  # down and right
                xmas_map[row + 1][col - 1],  # down and left
            ]

            curr_corners = "".join(corners)

            """
            M       M
                A
            S       S
            """

            if curr_corners in ["MMSS", "MSSM", "SSMM", "SMMS"]:
                count += 1

    return count


def main():
    with open(DATA_FILE, "r") as file:
        xmas_map = [list(line.strip()) for line in file]

    part_one_answer = part_one(xmas_map)
    print(f"{part_one_answer = }")

    part_two_answer = part_two(xmas_map)
    print(f"{part_two_answer = }")


if __name__ == "__main__":
    main()
