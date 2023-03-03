#!/usr/bin/env python3
import time

def get_row(line: str) -> int:
    # start range of rows is 0 through 127
    start = [x for x in range(0, 128)]

    for letter in line:
        # print(start)
        # time.sleep(1)
        half_length = len(start) // 2
        first_half, second_half = start[:half_length], start[half_length:]
        if letter == 'F':
            # take lower half
            start = first_half
        if letter == 'B':
            start = second_half
    
    return start[0]

def get_seat(line: str) -> int:
    start = [x for x in range(0, 8)]
    
    for letter in line:
        half_length = len(start) // 2
        first_half, second_half = start[:half_length], start[half_length:]
        if letter == 'R':
            start = second_half
        if letter == 'L':
            start = first_half
    
    return start[0]

def get_your_seat(seats: list) -> int:
    manifest = sorted(seats)
    # print(*(x for x in manifest), sep='\n')
    for num, person in enumerate(manifest, start=manifest[0][2]):
        # print(num, person)
        if num != person[2]:
            return num


def main():
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
    
    manifest = []
    
    for line in lines:
        row = get_row(line[:7])
        seat = get_seat(line[7:])
        seat_id = row * 8 + seat
        manifest.append((row, seat, seat_id))

    print(f"part one: {sorted(manifest)[-1]}")
    part_two = get_your_seat(manifest)
    print(f"{part_two = }")

if __name__ == "__main__":
    main()