#!/usr/bin/env python3

from copy import deepcopy


def process_line(line):
    open = ['(', '[', '{', '<']
    close = [')', ']', '}', '>']
    values = [3, 57, 1197, 25137]
    totals = [0, 0, 0, 0]
    processed = []

    for char in line:
        if char in open:  # opening char
            processed.append(char)

        else:   # closing char
            curr = processed.pop()
            idx = close.index(char)
            if curr != open[idx]:
                # invalid chunk
                totals[idx] += values[idx]

    return sum(totals)


def part_one(data):
    score = 0
    valid_lines = []
    for line in data:
        curr_score = process_line(line)
        if curr_score == 0:  # valid line, add to valid lines list
            valid_lines.append(line)
        else:
            score += curr_score

    return score, valid_lines


def part_two(valid_lines):
    total_score = []
    open = ['(', '[', '{', '<']
    scores = [1, 2, 3, 4]
    processed = []

    for line in valid_lines:
        for char in line:
            if char in open:
                processed.append(char)

            else:
                curr = processed.pop()

        curr_score = 0
        while processed:
            idx = open.index(processed.pop())
            curr_score = curr_score * 5
            curr_score += scores[idx]

        total_score.append(curr_score)

    return sorted(total_score)[len(total_score) // 2]


def main():
    with open("input.txt", "r") as file:
        data = [list(line.strip()) for line in file.readlines()]

    p1, valid_lines = part_one(deepcopy(data))
    print(f"Part One: {p1}")

    p2 = part_two(valid_lines)
    print(f"Part Two: {p2}")


if __name__ == "__main__":
    main()
