# AoC 2024, day

from functools import cache

SAMPLE2_FILE = "sample2.txt"
SAMPLE_FILE = "sample.txt"
DATA_FILE = "data.txt"


@cache
def process_stone(stone, count):
    if count == 0:
        return 1

    if stone == 0:
        return process_stone(1, count - 1)

    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        middle = len(stone_str) // 2
        left_result = process_stone(int(stone_str[:middle]), count - 1)
        right_result = process_stone(int(stone_str[middle:]), count - 1)
        return left_result + right_result

    else:
        return process_stone(stone * 2024, count - 1)


def process_stones(stones, count):
    total = 0
    for stone in stones:
        total += process_stone(stone, count)

    return total


def main():
    with open(DATA_FILE, "r") as file:
        stones = [int(x) for x in file.read().split()]

    print(f"{stones = }")

    part_one_answer = process_stones(stones, 25)
    print(f"{part_one_answer = }")

    part_two_answer = process_stones(stones, 75)
    print(f"{part_two_answer = }")


if __name__ == "__main__":
    main()
