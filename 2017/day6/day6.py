#!/usr/bin/env python3
import copy
import logging
import sys

# using logging to replace repetitive print statements
logger = logging.getLogger(__name__)  # creates logger object
logger.setLevel(logging.DEBUG)  # sets logging level
handler = logging.StreamHandler(sys.stdout)  # routes output to stdout
formatter = logging.Formatter(
    'Function[%(funcName)s] - Line [%(lineno)d] - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)  # adds handler to logger


def largest_idx(mem_list: list) -> int:
    largest_idx = 0
    largest_num = 0

    for num in range(0, len(mem_list)):
        if mem_list[num] > largest_num:
            largest_num = mem_list[num]
            largest_idx = num
    return largest_idx


def make_list_one_number(mem_list: list) -> int:
    mem_list = [str(element) for element in mem_list]
    new_integer = int(''.join(mem_list))
    return new_integer


def distribute(mem_list: list) -> list:
    new_list = copy.deepcopy(mem_list)
    start_idx = largest_idx(new_list)
    number_to_distribute = new_list[start_idx]
    new_list[start_idx] = 0 # set start idx to zero
    
    while number_to_distribute > 0:
        start_idx += 1
        new_list[start_idx % len(new_list)] += 1        
        number_to_distribute -= 1

    return new_list

def get_cycles(mem_list: list) -> int:
    been_there = []
    cycles = 0
    been_there.append(mem_list)
    while True:
        new_list = distribute(been_there[-1])
        if new_list in been_there:
            # print index of item
            idx_pos = been_there.index(new_list)
            print(f"{idx_pos = }")
            part_2 = len(been_there) - idx_pos
            return cycles + 1, part_2
        else:
            been_there.append(new_list)
            cycles += 1

def main():
    with open("input.txt") as file:
        line = file.readline()
        line = line.split("\t")

    memory = [int(i) for i in line]
    logger.debug(f" original: {memory}")
    part_1, part2 = get_cycles(memory)
    print(f"{part_1 = }")
    print(f"{part2 = }")


if __name__ == "__main__":
    main()
