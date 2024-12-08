# AoC 2024, day 7

import time
from copy import deepcopy
from itertools import product
from math import prod

SAMPLE_FILE = "sample.txt"
DATA_FILE = "data.txt"

is_part_two = False


def calculate_expression(numbers, operators):
    total = numbers[0]

    for i, op in enumerate(operators):
        if op == "+":
            total += numbers[i + 1]
        elif op == "*":
            total *= numbers[i + 1]
        elif op == "||":
            total = int(f"{total}{numbers[i + 1]}")

    return total


def try_perms(answer, numbers):
    if is_part_two:
        operator_combinations = product(["+", "*", "||"], repeat=len(numbers) - 1)

    else:
        operator_combinations = product(["+", "*"], repeat=len(numbers) - 1)

    for operators in operator_combinations:
        curr_expression = f"{numbers[0]}"
        for num, op in zip(numbers[1:], operators):
            curr_expression += f" {op} {num}"

        total = calculate_expression(numbers, operators)

        if total == answer:
            return True

    return False


def produces_result(result, numbers) -> bool:
    if sum(numbers) == result:
        return True

    if prod(numbers) == result:
        return True

    if len(numbers) < 2:
        return False

    return try_perms(result, numbers)


def part_one(equations) -> int:
    total = 0
    for eq in equations:
        if produces_result(eq[0], eq[1]):
            total += eq[0]
    return total


def main():
    start = time.time()

    with open(SAMPLE_FILE, "r") as file:
        data = [line.strip().split(": ") for line in file]

    equations = []
    for line in data:
        x, y = line
        y = list(map(int, y.split(" ")))
        equations.append([int(x), y])

    part_one_answer = part_one(deepcopy(equations))
    print(f"{part_one_answer = }")

    global is_part_two
    is_part_two = True  # turn on global bool

    part_two_answer = part_one(equations)
    print(f"{part_two_answer = }")

    end = time.time()
    print(f"Elapsed Time: {end - start:.2f} seconds.")


if __name__ == "__main__":
    main()
