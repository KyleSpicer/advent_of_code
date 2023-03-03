#! /usr/bin/env python3

def main():  

    with open("input.txt") as file:
        instructions = file.readline().strip()
    
    instructions = [x.strip() for x in instructions]
    houses = []
    santa = [0,0] # where santa begins
    RoboSanta = [0,0] # where santa begins
    houses.append(santa.copy())

    # for instruction in instructions:
        
    #     if instruction == '>':
    #         # east, x + 1
    #         santa[0] = (santa[0] + 1)
    #         if santa not in houses:
    #             houses.append(santa.copy())

    #     elif instruction == '<':
    #         # west, x - 1
    #         santa[0] = (santa[0] - 1)
    #         if santa not in houses:
    #             houses.append(santa.copy())

    #     elif instruction == '^':
    #         # north, y + 1
    #         santa[1] = (santa[1] + 1)
    #         if santa not in houses:
    #             houses.append(santa.copy())

        
    #     elif instruction == 'v':
    #         # south, y -1
    #         santa[1] = (santa[1] - 1)
    #         if santa not in houses:
    #             houses.append(santa.copy())
            
    
    # # print(len(houses))
    # print(f"part one = {len(houses)}")

    for num, instruction in enumerate(instructions):
        Real_Santa = False
        # even Santa, odd RoboSanta
        
        if (num % 2) == 0:
            Real_Santa = True
        else:
            Real_Santa = False

        if instruction == '>':
            # east, x + 1
            if Real_Santa:
                santa[0] = (santa[0] + 1)
                if santa not in houses:
                    houses.append(santa.copy())
            else:
                RoboSanta[0] = RoboSanta[0] + 1
                if RoboSanta not in houses:
                    houses.append(RoboSanta.copy())

        elif instruction == '<':
            # east, x + 1
            if Real_Santa:
                santa[0] = (santa[0] - 1)
                if santa not in houses:
                    houses.append(santa.copy())
            else:
                RoboSanta[0] = RoboSanta[0] - 1
                if RoboSanta not in houses:
                    houses.append(RoboSanta.copy())
        
        elif instruction == '^':
            if Real_Santa:
                santa[1] = (santa[1] + 1)
                if santa not in houses:
                    houses.append(santa.copy())
            else:
                RoboSanta[1] = RoboSanta[1] + 1
                if RoboSanta not in houses:
                    houses.append(RoboSanta.copy())
        
        elif instruction == 'v':
            if Real_Santa:
                santa[1] = (santa[1] - 1)
                if santa not in houses:
                    houses.append(santa.copy())
            else:
                RoboSanta[1] = RoboSanta[1] - 1
                if RoboSanta not in houses:
                    houses.append(RoboSanta.copy())

    print(f"part two = {len(houses)}")

if __name__ == "__main__":
    main()