#!/usr/bin/env python3

"""
Advent of Code 2021, Day 3
"""

import queue


def calculate_gamma_rate(data):
    g_rate = ""
    cols = len(data[0])
    curr_pos = 0

    while curr_pos < cols:
        ones = 0
        zeros = 0

        for rate in data:
            num = int(rate[curr_pos])
            if 0 == num:
                zeros += 1
            else:
                ones += 1

        if ones > zeros:
            g_rate = f"{g_rate}1"
        else:
            g_rate = f"{g_rate}0"

        curr_pos += 1

    return int(g_rate, 2)


def calculate_epsilon_rate(data):
    e_rate = ""
    curr_pos = 0
    cols = len(data[0])

    while curr_pos < cols:
        ones = 0
        zeros = 0

        for rate in data:
            num = int(rate[curr_pos])
            if 0 == num:
                zeros += 1
            else:
                ones += 1

        if ones > zeros:
            e_rate = f"{e_rate}0"
        else:
            e_rate = f"{e_rate}1"

        curr_pos += 1

    return int(e_rate, 2)


def part_one(lines):
    gamma_rate = calculate_gamma_rate(lines)
    epsilon_rate = calculate_epsilon_rate(lines)

    power_consumption = gamma_rate * epsilon_rate
    return power_consumption


def calculate_oxygen_gen_rating(oxy_q, cols):
    q_size = oxy_q.qsize()

    idx = 0
    while idx < cols:
        zeros = 0
        ones = 0
        for _ in range(q_size):
            item = oxy_q.get()
            if item[idx] == "0":
                zeros += 1
            else:
                ones += 1
            oxy_q.put(item)  # Put item back in queue after processing

        keeper = ""
        if ones >= zeros:
            keeper = "1"
        else:
            keeper = "0"

        keeper_q = queue.Queue()
        for _ in range(q_size):
            item = oxy_q.get()
            if item[idx] == keeper:
                keeper_q.put(item)
            else:
                oxy_q.put(item)  # Put non-keeper items back into the queue

        if keeper_q.qsize() == 1:
            ret_str = keeper_q.get()
            return int(ret_str, 2)
        oxy_q = keeper_q
        idx += 1


def calculate_co2_scrubber_rating(co2_q, cols):
    q_size = co2_q.qsize()

    idx = 0
    while idx < cols:
        zeros = 0
        ones = 0
        for _ in range(q_size):
            item = co2_q.get()
            if item[idx] == "0":
                zeros += 1
            else:
                ones += 1
            co2_q.put(item)  # Put item back in queue after processing

        keeper = ""
        if ones >= zeros:
            keeper = "0"
        else:
            keeper = "1"

        keeper_q = queue.Queue()
        for _ in range(q_size):
            item = co2_q.get()
            if item[idx] == keeper:
                keeper_q.put(item)
            else:
                co2_q.put(item)  # Put non-keeper items back into the queue

        if keeper_q.qsize() == 1:
            ret_str = keeper_q.get()
            return int(ret_str, 2)
        co2_q = keeper_q
        idx += 1


def part_two(lines):

    oxy_q = queue.Queue()
    co2_q = queue.Queue()
    for item in lines:
        oxy_q.put(item)
        co2_q.put(item)

    oxygen_gen_rating = calculate_oxygen_gen_rating(oxy_q, len(lines[0]))

    co2_scrubber_rating = calculate_co2_scrubber_rating(co2_q, len(lines[0]))

    return (oxygen_gen_rating * co2_scrubber_rating)


def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    part_one_answer = part_one(lines)
    print(f"{part_one_answer = }")

    part_two_answer = part_two(lines)
    print(f"{part_two_answer = }")


if __name__ == '__main__':
    main()
