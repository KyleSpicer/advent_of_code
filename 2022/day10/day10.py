#!/usr/bin/env python3

def part_one(data):
    # clock circuit ticks at a constant rate (cycle)
    cycles = 0

    # cpu single register, x starts at value of 1
    x = 1

    # Instruction: addx V takes two cycles to complete. After two cycles, the x register is increased by value.
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

def is_sprite_visible(sprite) -> bool:
    val = '#'

    if val in sprite:
        return True
    else:
        return False


def part_two(data):
    cycles = 0      # number of cycles
    x = 1           # register
    check = [40, 80, 120, 160, 200, 240]



def main():
    with open("sample.txt", "r") as file:
        data = [line.strip() for line in file.readlines()]
    
    p1 = part_one(data)
    print(f"Part One: {p1}")

    p2 = part_two(data)
    

if __name__=="__main__":
    main()
