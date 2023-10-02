#!/usr/bin/env python3

from copy import deepcopy
from collections import deque


def print_graph(graph):
    for line in graph:
        print(line)


def part_one(graph):
    # Find all low points in graph
    # risk level of low point is 1 plus its height.
    rows = len(graph)
    cols = len(graph[0])
    low_points = []
    risk_level = 0

    for x in range(rows):
        for y in range(cols):
            curr = graph[x][y]
            neighbors = []

            # left
            if y > 0:
                neighbors.append(graph[x][y - 1])
            # right
            if y < cols - 1:
                neighbors.append(graph[x][y + 1])
            # up
            if x > 0:
                neighbors.append(graph[x - 1][y])
            # down
            if x < rows - 1:
                neighbors.append(graph[x + 1][y])

            # check if num is low point between neighbors
            if all(num > curr for num in neighbors):
                low_points.append((x, y))
                risk_level += curr + 1

    return risk_level, low_points


def dfs(graph, x, y, visited):
    basin_size = 0
    rows = len(graph)
    cols = len(graph[0])

    if x < 0 or x >= rows or y < 0 or y >= cols:
        return 0

    if visited[x][y]:
        return 0
    else:
        visited[x][y] = True

    start = graph[x][y]
    if start == 9:
        return 0

    basin_size += 1

    basin_size += dfs(graph, x + 1, y, visited)   # down
    basin_size += dfs(graph, x - 1, y, visited)   # up
    basin_size += dfs(graph, x, y + 1, visited)   # right
    basin_size += dfs(graph, x, y - 1, visited)   # left

    return basin_size


def part_two(graph, low_points) -> int:
    basin_sizes = []
    visited = [[False for _ in range(len(graph[0]))]
               for _ in range(len(graph))]

    # depth first search
    for basin in low_points:
        basin_size = dfs(graph, basin[0], basin[1], visited)
        basin_sizes.append(basin_size)

    # find the three largest basins and multiply their sizes together
    basin_sizes = sorted(basin_sizes, reverse=True)

    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


def main():
    with open("input.txt", "r") as file:
        data = [line.strip() for line in file.readlines()]

    graph = []  # convert list of strings to list of ints
    for num_str in data:
        num_list = [int(char) for char in num_str]
        graph.append(num_list)

    p1, low_points = part_one(deepcopy(graph))
    print(f"Part One: {p1}")

    p2 = part_two(deepcopy(graph), low_points)
    print(f"Part Two: {p2}")


if __name__ == "__main__":
    main()
