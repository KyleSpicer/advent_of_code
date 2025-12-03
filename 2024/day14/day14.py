# AoC 2024, day14

from copy import deepcopy

SAMPLE_FILE = "sample.txt"
DATA_FILE = "data.txt"

sample_rows = 7
sample_cols = 11
data_rows = 103
data_cols = 101


def process_data(data) -> list:
    robot_movements = []

    for line in data:
        current = dict()
        p_line = line.split()[0]
        v_line = line.split()[1]

        px, py = p_line.split("=")[1].split(",")
        px, py = int(px), int(py)

        vx, vy = v_line.split("=")[1].split(",")
        vx, vy = int(vx), int(vy)

        current["p"] = (px, py)
        current["v"] = (vx, vy)

        robot_movements.append(current)

    return robot_movements


def update_grid(grid, movements, is_part_one):
    for movement in movements:
        px, py = movement["p"]
        if is_part_one:
            grid[py][px] = str(int(grid[py][px]) + 1)
        else:
            grid[py][px] = "#"

    return grid


def gen_grid(is_sample, is_part_one) -> list:
    grid = []
    if is_sample:
        rows = sample_rows
        cols = sample_cols
    else:
        rows = data_rows
        cols = data_cols

    for i in range(rows):
        row = []
        for j in range(cols):
            if is_part_one:
                row.append("0")
            else:
                row.append(".")

        grid.append(row)
    return grid


def update_movements(robot_movements, is_sample):
    if is_sample:
        rows = sample_rows
        cols = sample_cols
    else:
        rows = data_rows
        cols = data_cols

    for movement in robot_movements:
        px, py = movement["p"]
        vx, vy = movement["v"]
        movement["p"] = ((px + vx) % cols, (py + vy) % rows)

    return robot_movements


def calc_quadrants(grid, movements, is_sample, is_part_one):
    grid = update_grid(grid, movements, is_part_one)

    quadrants_results = []

    if is_sample:
        rows = sample_rows
        cols = sample_cols
    else:
        rows = data_rows
        cols = data_cols

    mid_row = rows // 2
    mid_col = cols // 2

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if i < mid_row and j < mid_col:
                q1 += int(grid[i][j])

            elif i < mid_row and j > mid_col:
                q2 += int(grid[i][j])

            elif i > mid_row and j < mid_col:
                q3 += int(grid[i][j])

            elif i > mid_row and j > mid_col:
                q4 += int(grid[i][j])

    return q1 * q2 * q3 * q4


def part_one(robot_movements, is_part_one, is_sample, seconds):
    result = 0

    if is_sample:
        if is_part_one:
            grid = gen_grid(True, True)
        else:
            grid = gen_grid(True, False)

    else:
        if is_part_one:
            grid = gen_grid(False, True)
        else:
            grid = gen_grid(False, False)

    if is_part_one:
        for second in range(seconds):
            robot_movements = update_movements(robot_movements, is_sample)

        result = calc_quadrants(grid, robot_movements, is_sample, is_part_one)

    else:
        for second in range(seconds):
            robot_movements = update_movements(robot_movements, is_sample)
            temp_grid = deepcopy(grid)
            temp_grid = update_grid(temp_grid, robot_movements, False)

            found = False
            if second > 7200:
                for row in temp_grid:
                    if "##########" in "".join(row):
                        found = True
                        result = second + 101
                        break

    return result


def main():
    with open(DATA_FILE, "r") as file:
        data = file.readlines()

    robot_movements = process_data(data)

    part_one_answer = part_one(robot_movements, True, False, 100)
    print(f"{part_one_answer = }")

    part_two_answer = part_one(robot_movements, False, False, 8000)
    print(f"{part_two_answer = }")


if __name__ == "__main__":
    main()
