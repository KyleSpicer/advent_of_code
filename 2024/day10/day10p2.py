SAMPLE_FILE = "sample.txt"
LARGE_SAMPLE_FILE = "larger_example.txt"
DATA_FILE = "data.txt"

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # west  # east  # north  # south


def display_map(topo_map):
    for line in topo_map:
        print(line)


def identify_trailheads(topo_map) -> list:
    """returns list of trailhead locations (tuples)"""
    trail_heads = []

    for row_i, row in enumerate(topo_map):
        for col_i, col in enumerate(row):
            if topo_map[row_i][col_i] == 0:
                trail_heads.append((row_i, col_i))

    return trail_heads


def bfs(topo_map, th_loc):
    start_x, start_y = th_loc
    visited = []
    value = topo_map[start_x][start_y]
    neighbors = []

    # get neighbors
    for dx, dy in directions:
        nx, ny = start_x + dx, start_y + dy
        if 0 <= nx < len(topo_map) and 0 <= ny < len(topo_map[0]):
            n_val = topo_map[nx][ny]

            if value + 1 == n_val:
                if n_val == 9:
                    visited.append((nx, ny))
                else:
                    neighbors.append((nx, ny))

    for n in neighbors:
        visited.extend(bfs(topo_map, n))

    return visited


def part_one(topo_map) -> int:
    total = 0
    result = 0
    trailheads = identify_trailheads(topo_map)
    for th_loc in trailheads:
        result = len(bfs(topo_map, th_loc))
        total += result

    return total


def main():
    with open(DATA_FILE, "r") as file:
        topo_map = [list(line.strip()) for line in file.readlines()]
        topo_map = [[int(x) for x in line] for line in topo_map]

    part_one_answer = part_one(topo_map)
    print(f"{part_one_answer = }")


if __name__ == "__main__":
    main()
