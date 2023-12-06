#!/usr/bin/env python3

from functools import reduce
from operator import mul

def process_race(race_info):
    """
    Your toy boat has a starting speed of zero millimeters per millisecond. For each whole millisecond you spend at the beginning of the race holding down the button, the boat's speed increases by one millimeter per millisecond.
    """
    
    ways_to_win = 0
    boat_speed = 0
    time = race_info[0]
    race_record = race_info[1]
    
    for secs_held in range(time):
        boat_speed = secs_held
        time_remaining = time - secs_held
        result = boat_speed * time_remaining
        if result > race_record:
            ways_to_win += 1

    return ways_to_win

def process_p1(races_info):
    results_total = [] 

    for race in races_info:
        results_total.append(process_race(race))

    return reduce(mul, results_total)
    
def process_p2(race_info):
    time = ''
    record_dist = ''

    for tup in race_info:
        time += str(tup[0])
        record_dist += str(tup[1])

    time = int(time)
    record_dist = int(record_dist)

    return process_p1([(time, record_dist)]) 

def main():
    data = open("sample.txt").read().split("\n")
    
    info = []
    for race in data:
        info.append(list(map(int, race.split(":")[1].split())))
    
    races_info = [tuple(pair) for pair in zip(info[0], info[1])]

    p1_answer = process_p1(races_info)
    print(f"{p1_answer = }")

    p2_answer = process_p2(races_info)
    print(f"{p2_answer = }")


if __name__=="__main__":
    main()