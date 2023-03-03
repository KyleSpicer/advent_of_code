#!/usr/bin/env python3

def count_twos(chars_count: dict) -> bool:
    result = any(value == 2 for value in chars_count.values())
    return result

def count_threes(chars_count: dict) -> bool:
    result = any(value == 3 for value in chars_count.values())
    return result
    

def pack_dict(line: str) -> dict:
    char_count = {}
    for letter in line.strip():
        if letter not in char_count.keys():
            char_count[letter] = 0    
        char_count[letter] += 1

    return char_count

def compare_strings(list_of_strings: list) -> list:
    
    results = []
    counter = 0
        
    for line in list_of_strings:
        print(line, end=" -- \n")
        for another_line in list_of_strings:
            curr_result = []
            if another_line == line:
                continue
            else:
                print(f"\t{another_line}")
                comb = zip(line, another_line)
                for i, j in comb:
                    # print(f"{i} -- {j}")
                    if i == j:
                        i = '-'
                        j = '-'
                    else:
                        curr_result.append((i, j))

            # print(f"{curr_result = }")
            results.append((line, another_line, curr_result))
    return results

def get_shortest_item_length(squished_list: list):

    shortest = []
    diff = 10

    for item in enumerate(squished_list):
        if len(item[1][2]) < diff:
            diff = len(item[1][2])
            shortest = []
            shortest.append(item)
    
    return diff, shortest
        

def main():
    with open("input.txt") as file:
        lines = file.readlines()
    
    # twos = 0
    # threes = 0
    
    # for line in lines:
    #     my_dict = pack_dict(line)
    #     contains_twos = count_twos(my_dict)
    #     if contains_twos:
    #         twos += 1
        
    #     contains_threes = count_threes(my_dict)
    #     if contains_threes:
    #         threes += 1
    
    # part_1 = twos * threes
    # print(part_1)

    all_lines = []

    for line in lines:
        line = line.strip()
        all_lines.append(line)

    squished = compare_strings(all_lines)
    shortest_idx, item = get_shortest_item_length(squished)
    
    print(f"{shortest_idx = }")
    print(item)

if __name__=="__main__":
    main()