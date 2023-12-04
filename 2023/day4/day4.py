#!/usr/bin/env python3

def calc_card(card):
    card_matches = 0
    card_value = 0

    winning, mine = card.split("|")
    winning = winning.split(" ")
    mine = mine.split(" ")

    filtered_winning = [int(item) for item in winning if item != '']
    filtered_mine = [int(item) for item in mine if item != '']

    for num in filtered_mine:
        if num in filtered_winning:
            card_matches += 1

    if card_matches < 2:
        return card_matches

    else:
        double_amount = card_matches - 1
        card_value = 1
        for _ in range(double_amount):
            card_value *= 2

        return card_value

def p2_calc_card(card):
    card_matches = 0

    winning, mine = card.split("|")
    winning = winning.split(" ")
    mine = mine.split(" ")

    filtered_winning = [int(item) for item in winning if item != '']
    filtered_mine = [int(item) for item in mine if item != '']

    for num in filtered_mine:
        if num in filtered_winning:
            card_matches += 1
    
    return card_matches

def process_p1(contents):
    total = 0
    for line in contents:
        total += calc_card(line)

    return total

def process_p2(contents):
    instances = [1] * len(contents)

    for idx in range(len(contents)):
        matches = p2_calc_card(contents[idx])
        for _ in range(instances[idx]):
            for num in range(matches):
                instances[idx + num + 1] += 1
            
    return sum(instances)

def main():
    with open("input.txt", "r") as file:
        contents = file.readlines()
        contents = [line.strip() for line in contents]
        contents = [line.split(":") for line in contents]
        contents = [line[1].strip() for line in contents]

    p1_answer = process_p1(contents)
    print(f"{p1_answer = }")

    p2_answer = process_p2(contents)
    print(f"{p2_answer = }")


if __name__=="__main__":
    main()