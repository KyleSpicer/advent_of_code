#!/usr/bin/env python3

import math

def part_one(mass: int) -> int:
    return math.floor(mass/3) - 2

def main():
    # to find the fuel required for a module:
    # take its mass, divide by three, round down, and subtract 2.
    with open("input.txt") as file:
        lines = file.readlines()
    
    fuel_requirements = 0

    for mass in lines:
        mass = int(mass)

        
        fuel = part_one(mass)
        fuel_requirements += fuel

        while fuel > 0:
            new_fuel = part_one(fuel)
            if new_fuel > 0:
                fuel_requirements += new_fuel
            fuel = new_fuel        



        
    # print(f"part one: {fuel_requirements}")
    print(f"part two = {fuel_requirements}")

if __name__ == "__main__":
    main()