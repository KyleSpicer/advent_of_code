#!/usr/bin/env python3

from time import sleep
from copy import deepcopy
import math

def part_one(graph, data) -> int:
    """
    line segments are x1, y1 -> x2, y2
    one end of line is x1, y1 
    other end of line is x2, y2
    """

    for line in data:
        x1, y1 = line[0]
        x2, y2 = line[1]

        if x1 != x2 and y1 != y2:
            continue

        if x1 == x2: 
            min = y1
            max = y2

            if max < min:
                min = y2
                max = y1
            
            for y in range(min, max + 1):
                graph[y][x1] += 1
        
        else:
            # vertical            
            min = x1
            max = x2

            if max < min:
                min = x2
                max = x1
            
            for x in range(min, max + 1):
                graph[y1][x] += 1
    
    total_twos = [1 for row in graph for num in row if num > 1]
    return (sum(total_twos))

def part_two(graph, data) -> int:

    for line in data:
        x1, y1 = line[0]
        x2, y2 = line[1]

        if x1 == x2: 
            min = y1
            max = y2

            if max < min:
                min = y2
                max = y1
            
            for y in range(min, max + 1):
                graph[y][x1] += 1
        
        elif y1 == y2:
            # vertical            
            min = x1
            max = x2

            if max < min:
                min = x2
                max = x1
            
            for x in range(min, max + 1):
                graph[y1][x] += 1
        
        else:
            # diagonal          
            x_dir = 1 if x1 < x2 else -1
            y_dir = 1 if y1 < y2 else -1

            for x in range(x1, x2 + x_dir, x_dir):
                    graph[y1][x] += 1
                    y1 += y_dir

    total_twos = [1 for row in graph for num in row if num > 1]
    return (sum(total_twos))

def display_graph(graph):
    for row in graph:
        print(" ".join(map(str,row)))

def gen_graph(largest_idx) -> list:
    zeros = [[0] * (largest_idx + 1) for _ in range(largest_idx + 1)]

    return zeros

def convert_data(data: list) -> (list, int):
    greatest_num = 0
    new_data = []

    for line in data:
        line = line.split("->")
        x1, x2 = line[0].split(",")
        y1, y2 = line[1].split(",")

        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        if x1 > greatest_num:
            greatest_num = x1
        elif x2 > greatest_num:
            greatest_num = x2
        elif y1 > greatest_num:
            greatest_num = y1
        elif y2 > greatest_num:
            greatest_num = y2

        new_line = [(x1, x2), (y1, y2)]
        new_data.append(new_line)

    return new_data, greatest_num

def main():
    with open("input.txt", "r") as file:
        data = file.readlines()
        data = [line.strip("\n") for line in data]

    data, greatest_idx = convert_data(data)

    graph = gen_graph(greatest_idx)

    part_one_answer = part_one(deepcopy(graph), data)
    print(f"{part_one_answer = }")

    part_two_answer = part_two(graph, data)
    print(f"{part_two_answer = }")

if __name__=="__main__":
    main()
