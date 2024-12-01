# Advent of Code: 2024, Day 1

SAMPLE_FILE = "sample.txt"
DATA_FILE = "data.txt"


def part_one(l_list, r_list) -> int:
    total_dist = 0

    l_sorted = sorted(l_list)
    r_sorted = sorted(r_list)

    for i in range(len(l_sorted)):
        total_dist += abs(l_sorted[i] - r_sorted[i])

    return total_dist


def part_two(l_list, r_list):
    total_similarity = 0

    for num in l_list:
        count = r_list.count(num)
        total_similarity += count * num

    return total_similarity


def main():
    with open(DATA_FILE, "r") as file:
        data = [list(map(int, line.split())) for line in file]

    l_list, r_list = zip(*data)
    l_list = list(l_list)
    r_list = list(r_list)

    part_one_answer = part_one(l_list.copy(), r_list.copy())
    print(f"Part One: {part_one_answer}")

    part_two_answer = part_two(l_list.copy(), r_list.copy())
    print(f"Part Two: {part_two_answer}")


if __name__ == "__main__":
    main()
