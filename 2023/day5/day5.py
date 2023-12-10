#!/usr/bin/env python3

from copy import deepcopy as dc

def process_seed(seed, map):
    for m in map:
        dst_range = m[0]
        src_range = m[1]
        step = m[2]

        if seed in range(src_range, src_range + step):
            return seed + (dst_range - src_range)

    return seed

def reverse_process_seed(seed, map):
    dst =  map[0]
    src = map[1]
    step = map[2]

    if seed in range(dst, dst + step):
          return seed + (src - dst)
    
    return None

def p1(seeds, maps):
    conv_maps = []

    # convert map strings to lists of integers
    for chunk in maps:
        chunk_str_list = list(chunk.split("\n"))
        new_map = [[int(val) for val in line.split()] for line in chunk_str_list[1:]]
        conv_maps.append(new_map)

    seed_numbers = []

    for seed in seeds:
        for map in conv_maps:
            seed = process_seed(seed, map)
        
        seed_numbers.append(seed)   
    
    return min(seed_numbers)

def p2(seeds, maps):
    conv_maps = []

    # convert map strings to lists of integers
    for chunk in maps:
        chunk_str_list = list(chunk.split("\n"))
        new_map = [[int(val) for val in line.split()] for line in chunk_str_list[1:]]
        conv_maps.append(new_map)

    conv_maps = list(reversed(conv_maps))
    seed_ranges = [(seeds[i], seeds[i + 1]) for  i in range(0, len(seeds), 2)]

    reverse_ranges = []
    for m in conv_maps:
        reverse_ranges.append(m)

    loc = -1
    found = False

    while not found:
        loc += 1
        seed = loc
        for chunk in reverse_ranges:
            try:
                for dst, src, step in chunk:
                    if seed in range(dst, (dst + step)):
                        seed += src - dst
                        break
            except ValueError:
                pass
            
        for seed_range in seed_ranges:
            if seed in range(seed_range[0], seed_range[0] + seed_range[1]):
                found = True
                return loc
    
    return loc

def main():
    # unpack data
    seeds, *maps = open("input.txt").read().split("\n\n")
    seeds = list(map(int, seeds.split(":")[1].split()))

    p1_answer = p1(seeds, maps)
    print(f"{p1_answer = }")

    p2_answer = p2(seeds, maps)
    print(f"{p2_answer = }")



if __name__=="__main__":
    main()