#!/usr/bin/env python3

from copy import deepcopy
from itertools import permutations

# 0: 6
# 1: 2
# 2: 5
# 3: 5
# 4: 4
# 5: 5
# 6: 6
# 7: 3
# 8: 7
# 9: 6

auth = ["a", "b", "c", "d", "e", "f", "g"]
count = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def part_two(data):
    m = {"acedgfb": 8, "cdfbe": 5, "gcdfa": 2, "fbcad": 3, "dab": 7,
         "cefabd": 9, "cdfgeb": 6, "eafb": 4, "cagedb": 0, "ab": 1}

    m = {"".join(sorted(k)): v for k, v in m.items()}

    ans = 0
    for line in data:
        a, b = line.split(" | ")
        a = a.split(" ")
        b = b.split(" ")
        for perm in permutations("abcdefg"):
            pmap = {a: b for a, b in zip(perm, "abcdefg")}
            anew = ["".join(pmap[c] for c in x) for x in a]
            bnew = ["".join(pmap[c] for c in x) for x in b]
            if all("".join(sorted(an)) in m for an in anew):
                bnew = ["".join(sorted(x)) for x in bnew]
                ans += int("".join(str(m[x]) for x in bnew))
                break

    return ans


def part_one(data):
    answer = 0
    delim = "|"
    easy_count = [2, 4, 3, 7]

    for line in data:
        line = line.split(delim)
        easy_keys = line[1].split(" ")
        easy_keys = easy_keys[1:]

        for key in easy_keys:
            if all(char in auth for char in key):
                if len(key) in easy_count:
                    answer += 1
            else:
                print("invalid")

    return answer


def main():
    with open("sample.txt", "r") as file:
        data = file.readlines()
        data = [line.strip() for line in data]

    part_one_answers = part_one(deepcopy(data))
    print(f"{part_one_answers = }")

    part_two_answers = part_two(deepcopy(data))
    print(f"{part_two_answers = }")


if __name__ == "__main__":
    main()
