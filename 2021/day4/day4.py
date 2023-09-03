#!/usr/bin/env python3
import queue


def gen_bingo_cards(input) -> list:
    values = [int(value) for line in input if line.strip()
              for value in line.split()]

    chunk_size = 5
    chunks = [values[i:i + chunk_size]
              for i in range(0, len(values), chunk_size)]

    bingo_cards = []
    curr_card = []
    curr_idx = 0
    for chunk in chunks:
        curr_card.append(chunk)
        curr_idx += 1

        if 0 == curr_idx % chunk_size:
            bingo_cards.append(curr_card)
            curr_card = []

    return bingo_cards


def print_card(card):
    print("---------------")
    for row in card:
        for num in row:
            print(f"{num} ", end="")
        print()
    print("---------------")


def process_card_with_curr_num(card, curr_num):
    rows = len(card)
    cols = len(card[0])

    for row in range(rows):
        for col in range(cols):
            if card[row][col] == curr_num:
                card[row][col] = -1


def is_all_negative_ones(row):
    return all(value == -1 for value in row)


def check_card(card):
    rows = len(card)
    cols = len(card[0])

    for row in card:
        if is_all_negative_ones(row):
            return True

    for col in range(cols):
        if is_all_negative_ones([card[row][col] for row in range(rows)]):
            return True

    return False


def part_one(bingo_cards, bingo_nums):
    cards = queue.Queue()
    for card in bingo_cards:
        cards.put(card)

    for num in bingo_nums:
        tempq = queue.Queue()

        while not cards.empty():
            curr_card = cards.get()
            process_card_with_curr_num(curr_card, num)

            # check curr card for completion
            if True == check_card(curr_card):
                return num, curr_card

            tempq.put(curr_card)

        while not tempq.empty():
            cards.put(tempq.get())

    return 0


def calc_part_one(card, num):
    total = 0
    for row in card:
        for idx in row:
            if idx != -1:
                total += idx

    return total * num


def check_qty_complete(q):
    total_complete = 0
    while not q.empty():
        card = q.get()
        if card.completed:
            total_complete += 1

    return total_complete


def part_two(bingo_cards, bingo_nums):
    cards = queue.Queue()
    completed_cards = []

    for card in bingo_cards:
        cards.put(card)

    count = cards.qsize()

    for num in bingo_nums:
        tempq = queue.Queue()

        while not cards.empty():
            curr_card = cards.get()
            process_card_with_curr_num(curr_card, num)

            # check curr card for completion
            if True == check_card(
                    curr_card) and curr_card not in completed_cards:
                if len(completed_cards) == count - 1:
                    return num, curr_card
                else:
                    completed_cards.append(curr_card)

            tempq.put(curr_card)

        while not tempq.empty():
            cards.put(tempq.get())

    return 0, 0


def main():
    bingo_nums = []
    bingo_cards = []

    with open("input.txt", "r") as file:
        line = file.readline()
        bingo_nums = [int(num) for num in line.split(",")]

        remaining = file.readlines()

    bingo_cards = gen_bingo_cards(remaining)
    second_cards = gen_bingo_cards(remaining)

    curr_num, curr_card = part_one(bingo_cards, bingo_nums)
    part_one_result = calc_part_one(curr_card, curr_num)
    print(f"{part_one_result = }")

    second_num, second_card = part_two(second_cards, bingo_nums)
    part_two_result = calc_part_one(second_card, second_num)
    print(f"{part_two_result = }")


if __name__ == "__main__":
    main()
