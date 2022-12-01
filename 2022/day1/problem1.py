#! /usr/bin/env python3

def main():
    
    with open("problem1.txt", "r") as file:
        
        number_elf = 0
        number_elf_calories = 0
        highest_calorie_count = 0
        calorie_list = []
        
        for line in file:
            if line == '\n':
                if number_elf_calories > highest_calorie_count:
                    highest_calorie_count = number_elf_calories
                calorie_list.append(number_elf_calories)
                number_elf_calories = 0
                number_elf += 1
                
            else: 
                number_elf_calories += int(line)
            
        print(f"problem 1, part 1: {highest_calorie_count}")
        calorie_list.sort(reverse=True)
        # print(calorie_list)

        calorie_list = []
        for elf in range(3):
            calorie_list.append(calorie_list[elf])

        print(f"problem 1, part 2: {sum(calorie_list)}")


if __name__ == "__main__":
    main()
