# AoC 2024, day 5

SAMPLE_FILE = "sample.txt"
DATA_FILE = "data.txt"


def validate_update(rules, update):
    idx_dict = {}

    for i, num in enumerate(update):
        idx_dict[num] = i

    for a, b in rules:
        if a in idx_dict and b in idx_dict:
            if not idx_dict[a] < idx_dict[b]:
                return False
    return True


def part_one(rules, updates):
    total = 0
    bad_updates = []

    for update in updates:
        is_valid = validate_update(rules, update)
        if not is_valid:
            bad_updates.append(update)
        else:
            total += update[len(update) // 2]  # return middle number

    return total, bad_updates


def sort_update(rules, update) -> int:
    while True:
        is_correct = True
        for i in range(len(update) - 1):
            if [update[i + 1], update[i]] in rules:
                is_correct = False
                update[i], update[i + 1] = update[i + 1], update[i]

        if is_correct:
            return update[len(update) // 2]


def part_two(rules, bad_updates):
    total = 0

    for update in bad_updates:
        total += sort_update(rules, update)

    return total


def main():
    with open(DATA_FILE, "r") as file:
        rules, updates = file.read().split("\n\n")

    rules = [list(map(int, x.split("|"))) for x in rules.split("\n")]
    updates = [list(map(int, x.split(","))) for x in updates.split("\n")]

    part_one_answer, bad_updates = part_one(rules, updates)
    print(f"{part_one_answer = }")

    part_two_answer = part_two(rules, bad_updates)
    print(f"{part_two_answer = }")


if __name__ == "__main__":
    main()
