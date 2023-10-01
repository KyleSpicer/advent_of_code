#!/usr/bin/env python3

from copy import deepcopy

def print_graph(graph):
    for line in graph:
        print(line)

def part_one(graph):
    # Find all low points in graph
    # risk level of low point is 1 plus its height.
    rows = len(graph)
    cols = len(graph[0])
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
                risk_level += curr + 1

    return risk_level

def part_two(graph):
    # 
    three_basins_result = 0


    return three_basins_result

def main():
    with open("input.txt", "r") as file:
        data = [line.strip() for line in file.readlines()]

    graph = [] # convert list of strings to list of ints
    for num_str in data:
        num_list = [int(char) for char in num_str]    
        graph.append(num_list)
    
    p1 = part_one(deepcopy(graph))
    print(f"Part One: {p1}")

    p2 = part_two(deepcopy(graph))
    print(f"Part Two: {p2}")


if __name__=="__main__":
    main()
