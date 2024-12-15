# AoC 2024, day 12

SAMPLE_FILE = "sample.txt"
LSAMPLE_FILE = "large_sample.txt"
DATA_FILE = "data.txt"

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def display_grid(grid):
    for line in grid:
        print(line)


def mark_region(grid, visited, start_x, start_y) -> list:
    region = set()
    stack = [(start_x, start_y)]
    region.add((start_x, start_y))
    region_char = grid[start_x][start_y]

    while stack:
        x, y = stack.pop(0)
        for dx, dy in directions:
            neighbor_x, neighbor_y = x + dx, y + dy
            if 0 <= neighbor_x < len(grid) and 0 <= neighbor_y < len(grid[0]):
                if grid[neighbor_x][neighbor_y] == region_char:
                    n = (neighbor_x, neighbor_y)
                    region.add(n)
                    if n not in visited:
                        visited.add(n)
                        stack.append(n)

    return list(region)


def calc_price(grid, region):
    area = len(region)
    perimeter = 0

    for x, y in region:
        same_neighbors = 0
        curr_char = grid[x][y]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                neighbor_char = grid[nx][ny]

                if neighbor_char == curr_char:
                    same_neighbors += 1

        perimeter += 4 - same_neighbors

    return area * perimeter


def in_grid(coord, max_row, max_col) -> bool:
    x, y = coord
    return 0 <= x < max_row and 0 <= y < max_col


def calc_price2(grid, region) -> int:
    corners = 0

    if len(region) == 1:
        return 4

    for plot in region:
        x, y = plot

        N = (x - 1, y) in region
        E = (x, y + 1) in region
        S = (x + 1, y) in region
        W = (x, y - 1) in region

        NE = (x - 1, y + 1) in region
        NW = (x - 1, y - 1) in region
        SE = (x + 1, y + 1) in region
        SW = (x + 1, y - 1) in region

        # outside top left corner
        if not N and not W and (E or S):
            corners += 1

        # outside top right corner
        if not N and not E and (W or S):
            corners += 1

        # outside bottom left corner
        if not S and not W and (E or N):
            corners += 1

        # outside bottom right corner
        if not S and not E and (W or N):
            corners += 1

        # inside corners
        if N and W and not NW:
            corners += 1

        if N and E and not NE:
            corners += 1

        if S and W and not SW:
            corners += 1

        if S and E and not SE:
            corners += 1

    return corners * len(region)


def generate_regions(grid, is_p2) -> list:
    visited = set()
    regions = []
    total = 0

    # generate regions
    for row_i, row in enumerate(grid):
        for col_i, col in enumerate(row):
            if (row_i, col_i) in visited:
                # already processed
                continue

            region = mark_region(grid, visited, row_i, col_i)
            regions.append(region)

    for region in regions:
        if not is_p2:
            price = calc_price(grid, region)
            total += price
        else:
            region_price = calc_price2(grid, region)
            total += region_price

    return total


def main():
    with open(DATA_FILE, "r") as file:
        grid = [list(line.strip()) for line in file.readlines()]

    part_one_answer = generate_regions(grid, False)
    print(f"{part_one_answer = }")

    part_two_answer = generate_regions(grid, True)
    print(f"{part_two_answer = }")


if __name__ == "__main__":
    main()
