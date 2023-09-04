#!/usr/bin/env python3.8
import queue
import sys
import math


def part_one(positions):
    pos = queue.Queue()

    for item in positions:
        pos.put(item)

    least_fuel = sys.maxsize
    least_fuel_pos = 0

    while not pos.empty():
        curr = pos.get()
        fuel = 0

        for item in positions:
            fuel += abs(curr - item)

        if fuel < least_fuel:
            least_fuel = fuel

    return least_fuel


def part_two(positions):

    l = len(positions)
    f = []

    for v in range(l):
        diff = [abs(d - v) for d in positions]
        diffs = sum([sum(list(range(dif + 1))) for dif in diff])
        f.append(diffs)

    return min(f)


def main():
    with open("input.txt", "r") as file:
        line = file.readline()
        positions = [int(pos) for pos in line.split(",")]

    part_one_result = part_one(positions)
    print(f"{part_one_result = }")

    part_two_result = part_two(positions)
    print(f"{part_two_result = }")


if __name__ == "__main__":
    main()
