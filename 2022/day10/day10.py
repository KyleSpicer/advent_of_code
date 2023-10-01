#!/usr/bin/env python3

def part_one(data):
    # clock circuit ticks at a constant rate (cycle)
    cycles = 0

    # cpu single register, x starts at value of 1
    x = 1

    # Instruction: addx V takes two cycles to complete. After two cycles, the
    # x register is increased by value.
    cycle_count = 2

    # Instruction: noop takes one cycle to complete, no other effect.

    # signal strength: cycle number * value of x register
    # during the 20th, 60th, 100th, 140th, 180th, 220th cycles
    check = [20, 60, 100, 140, 180, 220]

    sum = 0

    for line in data:
        if len(line) == 4:
            # noop instruction
            cycles += 1
            # check signal strength
            if cycles in check:
                sum += cycles * x

        else:
            ins, amount = line.split(" ")
            for cycle in range(cycle_count):
                cycles += 1
                # check sig strength
                if cycles in check:
                    sum += cycles * x

            x += int(amount)

    return sum


def is_sprite_visible(sprite, cycle) -> bool:
    val = '#'

    if 0 <= cycle <= 39:
        if sprite[cycle] == '#':
            return True

    else:
        return False


def display_crt(crt):
    for row in crt:
        print(''.join(row))


def update_sprite(sprite, x) -> list:
    pos = [x - 1, x, x + 1]

    new_sprite = list("........................................")

    for p in pos:
        if 0 <= p <= 39:
            new_sprite[p] = '#'

    return new_sprite


def part_two(data):
    cycle = 0      # number of cycles
    x = 1           # register number
    check = [40, 80, 120, 160, 200, 240]
    sprite = list("###.....................................")
    curr_crt = []
    crt = []

    for line in data:
        if len(line) == 4:  # noop instruction
            if is_sprite_visible(sprite, cycle % 40):
                curr_crt.append('#')
            else:
                curr_crt.append('.')

            cycle += 1
            if cycle in check:
                crt.append(curr_crt)
                curr_crt = []

        else:
            instruction, amount = line.split(" ")

            if is_sprite_visible(sprite, cycle % 40):
                curr_crt.append('#')
            else:
                curr_crt.append('.')

            cycle += 1
            if cycle in check:
                crt.append(curr_crt)
                curr_crt = []

            if is_sprite_visible(sprite, cycle % 40):
                curr_crt.append('#')
            else:
                curr_crt.append('.')

            cycle += 1
            if cycle in check:
                crt.append(curr_crt)
                curr_crt = []

            x += int(amount)
            sprite = update_sprite(sprite, x)

    display_crt(crt)


def main():
    with open("input.txt", "r") as file:
        data = [line.strip() for line in file.readlines()]

    p1 = part_one(data)
    print(f"Part One: {p1}")

    p2 = part_two(data)


if __name__ == "__main__":
    main()
