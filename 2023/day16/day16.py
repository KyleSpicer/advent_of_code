#!/usr/bin/env python3

from sys import argv
from collections import deque, defaultdict

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1),
}

def display_energized_map(graph, visited):

    new_graph = graph

    for v in visited:
        new_graph[v[0]][v[1]] = '#'
    
    print_graph(new_graph)

def print_graph(graph):
    for row in graph:
        for col in row:
            print(col, end='')
        print()

def part_one(graph):
    q = deque()
    q.append((0, -1, 'R'))
    seen_states = set()

    while q:
        curr = q.popleft()
        x, y, dir = curr
        dr, dc = directions.get(dir)

        x += dr
        y += dc

        # bounds check
        if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]):
            continue
        
        if (x, y, dir) in seen_states:
            continue
        seen_states.add((x, y, dir))
        
        char = graph[x][y]

        if '.' == char:
            q.append((x, y, dir))

        if '|' == char:
            if 'R' == dir or 'L' == dir:
                q.append((x, y, 'U'))
                q.append((x, y, 'D'))
            else:
                q.append((x, y, dir))

        if '-' == char:
            if 'U' == dir or 'D' == dir:
                    q.append((x, y, 'R'))
                    q.append((x, y, 'L'))
            else:
                q.append((x, y, dir))            
        
        if '\\' == char:
            new_dir = {'R': 'D', 'L': 'U', 'U': 'L', 'D': 'R'}
            q.append((x, y, new_dir[dir]))

        if '/' == char:
            new_dir = {'R': 'U', 'L': 'D', 'U': 'R', 'D': 'L'}
            q.append((x, y, new_dir[dir]))

    slimmed_seen_set = {(x, y) for x, y, _ in seen_states}
    # display_energized_map(graph, seen_states)
    print(f"Part One: {len(slimmed_seen_set)}")

def process_part_two(graph, x, y, dir):
    q = deque()
    q.append((x, y, dir))
    seen_states = set()

    while q:
        curr = q.popleft()
        x, y, dir = curr
        dr, dc = directions.get(dir)

        x += dr
        y += dc

        # bounds check
        if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]):
            continue
        
        if (x, y, dir) in seen_states:
            continue
        seen_states.add((x, y, dir))
        
        char = graph[x][y]

        if '.' == char:
            q.append((x, y, dir))

        if '|' == char:
            if 'R' == dir or 'L' == dir:
                q.append((x, y, 'U'))
                q.append((x, y, 'D'))
            else:
                q.append((x, y, dir))

        if '-' == char:
            if 'U' == dir or 'D' == dir:
                    q.append((x, y, 'R'))
                    q.append((x, y, 'L'))
            else:
                q.append((x, y, dir))            
        
        if '\\' == char:
            new_dir = {'R': 'D', 'L': 'U', 'U': 'L', 'D': 'R'}
            q.append((x, y, new_dir[dir]))

        if '/' == char:
            new_dir = {'R': 'U', 'L': 'D', 'U': 'R', 'D': 'L'}
            q.append((x, y, new_dir[dir]))

    slimmed_seen_set = {(x, y) for x, y, _ in seen_states}
    return len(slimmed_seen_set)

def part_two(graph):
    rows = len(graph)
    cols = len(graph[0])

    starting_points = deque()
    starting_points_record = defaultdict()

    for r in range(rows):
        starting_points.append((r, -1, 'R'))
        starting_points.append((r, rows, 'L'))

    for c in range(cols):
        starting_points.append((-1, c, 'D'))
        starting_points.append((rows, c, 'U'))

    while starting_points:
        curr = starting_points.popleft()
        starting_points_record[curr] = process_part_two(graph, *curr)

    print(f"Part Two: {max(starting_points_record.values())}")


def main():
    if 2 != len(argv):
        print(f"Usage: {argv[0]} <filename>")
        return
    
    with open(argv[1], "r") as file:
        data = [line.strip() for line in file.readlines()]
        data = [list(line) for line in data]
    
    part_one(data)
    part_two(data)

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
