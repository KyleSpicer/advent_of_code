#!/usr/bin/env python3

def part_one(instruction: list) -> int:
    # positive numbers ("forward") move downward -1
    # negative numbers ("backward"), move upward +1
    
    limit = len(instruction) # grabs length of list 


    idx = 0
    new_idx = 0
    steps = 0
    
    while True:
        try:
            new_idx += instruction[idx]

            if instruction[idx] >= 3:
                instruction[idx] -= 1
            else:
                instruction[idx] += 1

            idx = new_idx

            steps += 1

        except:
            return steps


        

def main():
    with open("input.txt") as file:
        lines = file.readlines()

    big_list = []

    for line in lines:
        big_list.append(int(line))


    part1 = part_one(big_list)
    print(f"{part1 = }")

if __name__=="__main__":
    main()  