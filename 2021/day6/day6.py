#!/usr/bin/env python3

import queue

# Notes:
# each laternfish creates a new fish once every 7 days
# model each fish as a single number that represents the number of days until it creates a new laternfish
# Each new laternfish will have a timer of 8 days
# the day after 0, it's timer would be reset to 6 and create a new laternfish with an internal timer of 8
# 

def display_fish_q(day, q):
    fish_list = list(q.queue)
    print(f"Day {day}: {fish_list}")

def add_new_day_8(original_queue, day_8_fish):
    original_queue.put(day_8_fish)

def update_day_6(original_queue, update_val):
    temp_q = queue.Queue()

    for _ in range(6):
        temp_q.put(original_queue.get())

    updated_fish = original_queue.get() + update_val
    temp_q.put(updated_fish)

    while not original_queue.empty():
        temp_q.put(original_queue.get())
    

    while not temp_q.empty():
        original_queue.put(temp_q.get())

def sum_all_fish(fish_q) -> int:
    total_sum = 0
    while not fish_q.empty():
        element = fish_q.get()
        total_sum += element

    return total_sum

def main():
    with open("input.txt", "r") as file:
        fish = file.readline().split(",")

    # create fish list from input
    fish = [int(fish_str) for fish_str in fish]

    # create 0-9 days list
    calendar = [0 for _ in range(9)]

    # add number of fish to calendar list to start with
    for f in fish:
        calendar[f] += 1

    # populate initial queue
    fish_queue = queue.Queue()
    for day in calendar:
        fish_queue.put(day)

    # start processing
    end_day = 256
    curr_day = 0

    while (curr_day < end_day):
        day_0 = (fish_queue.get())
        
        update_day_6(fish_queue, day_0)
        add_new_day_8(fish_queue, day_0)
        
        curr_day += 1

    total_fish = sum_all_fish(fish_queue)
    print(f"Total fish after day  {curr_day}: {total_fish}")

if __name__=="__main__":
    main()
