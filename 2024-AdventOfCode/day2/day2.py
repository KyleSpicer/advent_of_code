# AoC 2024, day 2

from itertools import pairwise

SAMPLE_FILE = "sample.txt"
DATA_FILE = "data.txt"

MIN = 1
MAX = 3
INCREASING = 1
DECREASING = 2


def is_increasing_or_decreasing(level) -> int:
    if all(a < b for a, b in pairwise(level)):
        return INCREASING

    elif all(a > b for a, b in pairwise(level)):
        return DECREASING
    else:
        return 0


def is_level_safe(level) -> bool:
    # all increasing or decreasing
    status = is_increasing_or_decreasing(level)

    if INCREASING == status:
        if all(MIN <= b - a <= MAX for a, b in pairwise(level)):
            return True

    elif DECREASING == status:
        if all(MIN <= a - b <= MAX for a, b in pairwise(level)):
            return True
    else:
        return False


def problem_dampener(level):
    level = level.copy()
    previous = 0

    for i, num in enumerate(level):
        curr_level = level.copy()
        curr_level.pop(i)
        safe = is_level_safe(curr_level)
        if safe:
            return True

    return False


def part_one(data):
    safe_levels = 0

    for level in data:
        safe = is_level_safe(level)
        if safe:
            safe_levels += 1

    return safe_levels


def part_two(data):
    safe_levels = 0

    for level in data:
        safe = is_level_safe(level)
        if safe:
            safe_levels += 1

        else:
            is_safe = problem_dampener(level)
            if is_safe:
                safe_levels += 1

    return safe_levels


def main():
    with open(DATA_FILE, "r") as file:
        data = [list(map(int, line.split())) for line in file]

    part_one_answer = part_one(data.copy())
    print(f"{part_one_answer = }")

    part_two_answer = part_two(data.copy())
    print(f"{part_two_answer = }")


if __name__ == "__main__":
    main()
