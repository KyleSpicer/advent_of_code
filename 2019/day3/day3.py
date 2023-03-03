#!/usr/bin/env python3

import time

def get_loop_size(subject_number) -> int:
    value = 1
    loop_size = 1
    remainder = 20201227

    while value != subject_number:
        value = value * subject_number
        print(value)
        time.sleep(2)
        value  %= remainder
        print(value)
        time.sleep(2)

        # print(value)
        if value == subject_number:
            return loop_size
        else:
            loop_size += 1

def main():
    with open("sample.txt") as file:
        lines = file.readlines()

    lines = [int(line.strip()) for line in lines]

    print(lines)
    for key in lines:
        answer = get_loop_size(key)
        print(f"answer = {answer}")



if __name__=="__main__":
    main()