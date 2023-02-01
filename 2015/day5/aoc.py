#!/usr/bin/env python3

# def bad_combo(line: str) -> bool:
#     bad = ['ab', 'cd', 'pq', 'xy']

#     i = 0
#     j = 1
#     while j < len(line):
#         check = line[i] + line[j]
#         if check in bad:
#             return True
#         else:
#             i += 1
#             j += 1
#     return False

# def vowel_count(line: str) -> int:
#     # atleast three vowels
#     count = 0
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for letter in line:
#         if letter in vowels:
#             count += 1
#     return count

# def check_double_letter(line: str) -> bool:
#     i = 0
#     j = 1
#     while j < len(line):
#         check = line[i] + line[j]
#         if check[0] == check[1]:
#             return True
#         else:
#             i += 1
#             j += 1
#     return False

# def p1_naughty_or_nice(line: str) -> str:
#     good = "nice"
#     bad = "naughty"

#     vowels = vowel_count(line)
#     if vowels < 3:
#         return bad

#     # returns True if bad combo exists in line
#     combo_check = bad_combo(line)
#     if combo_check:
#         return bad

#     double_letter = check_double_letter(line)
#     if not double_letter:
#         return bad


#     return good

def check_repeating_pairs(line: str) -> bool:
    # - It contains a pair of any two letters that appears at least twice in 
    # the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but 
    # not like aaa (aa, but it overlaps).
    twos_counter = {}
    threes_counter = set()

    old_chunk = ""

    for idx in range(len(line)):
        chunk = line[idx:idx+3]
        if len(chunk) > 2:
            if chunk[:-1] != old_chunk:
                twos_counter[chunk[:-1]] = twos_counter.get(chunk[:-1], 0) + 1
                old_chunk = chunk[:-1]
            else:
                old_chunk = ""
                
            threes_counter.add(chunk)
        else:
            if chunk != old_chunk:
                twos_counter[chunk] = twos_counter.get(chunk, 0) + 1
            break
        
        
    print(twos_counter)
    print(threes_counter)
    part1 = False
    for val in twos_counter.values():
        if val > 1:
            part1 = True
            break
        
    part2 = False
    for item in threes_counter:
        if item[0] == item[-1]:
            part2 = True
    print(part1 and part2)
    # return part1 and part2
    if part1 and part2:
        return True
    else:
        return False

def p2_naughty_or_nice(line: str) -> str:

    # - It contains at least one letter which repeats with exactly one letter 
    # between them, like xyx, abcdefeghi (efe), or even aaa.
    
    good = "nice"
    bad = "naughty"
    line = line.strip()
    print(line)
    
    # checks for duplicates first
    part2 = check_repeating_pairs(line)
    if part2:
        return good

    return bad


def main():
    f = open("input1.txt", "r")
    lines = f.readlines()

    nice = 0
    naughty = 0

    # for line in lines:
    #     result = p1_naughty_or_nice(line)
    #     if "nice" == result:
    #         nice += 1
    #     else:
    #         naughty += 1
    # print(f"Problem 1: {nice = }")

    for line in lines:
        result = p2_naughty_or_nice(line)
        print()
        if "nice" == result:
            nice += 1
        else:
            naughty += 1

    print(f"\n\nProblem 2: {nice = }")
    print(f"Problem 2: {naughty = }")


if __name__ == "__main__":
    main()
