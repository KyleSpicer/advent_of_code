#! /usr/bin/env python3


def create_list(num1, num2):
    if (num1 == num2):
        return [num1]
    else:
        newlist = []
        while(num1 < num2 + 1):
            newlist.append(num1)
            num1 += 1
    # print(f"{newlist = }")
    if len(newlist) > 1:
        return newlist
    else:
        return [newlist, 99]

def main():

    file = open("input.txt", "r")
    lines = file.readlines()

    group = 0 # keep track of line numbers
    first_elf = []
    second_elf = []

    pairs = 0
    
    for line in lines:
        group += 1
        print(f"{group = }")
        print(line, end="")
        line.strip()
        
        # my_list = re.split(r',', line)
        my_list = line.split('-')
        new_list = my_list[1].split(',')
        
        final_list = []
        final_list.append(my_list[0])
        final_list.append(new_list[0])
        final_list.append(new_list[1])
        final_list.append(my_list[2])
        
        print(final_list)
        
                
        # create list from number range for each elf
        first_elf = create_list(int(final_list[0]), int(final_list[1]))
        second_elf = create_list(int(final_list[2]), int(final_list[3]))

        print(f"{first_elf = }")
        print(f"{second_elf = }")
        
        elf_one = first_elf
        elf_two = second_elf
        
        elf_1 = first_elf
        elf_2 = second_elf
        
        # compare lists
        check_list_1 = any(item in first_elf for item in second_elf)
        print(f"{check_list_1 = }")
        
        if (check_list_1 == False):
            check_list_2 = any(item in second_elf for item in first_elf)
        
        print(f"{check_list_2 = }")
        
        if check_list_1 or check_list_2 == True:
            pairs += 1
        
        
        
                
        print()
    print(f"{pairs = }")  

if __name__ == "__main__":
    main()