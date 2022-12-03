#! /usr/bin/env python3

from itertools import islice

def main():
    # notes
    # 
    # pocket1 = []
    # pocket2 = []
    
    sum_for_all_groups = 0
    
    group = 0 # counter for groups
    
    with open("input.txt", "r") as file:
        while True:
            line1 = file.readline()
            if not line1:
                break
            else:
                group += 1
                line2 = file.readline()
                line3 = file.readline()
                print(f"{group = }")
                print(f"{line1 = }")
                print(f"{line2 = }")
                print(f"{line3 = }")
                
                in_all = []
                for char in line1:
                    if char in line2 and char in line3 and char != '\n':
                        in_all.append(char)
                        
                
                print(f"{in_all = }")
        
            converted_num= 0 
            for char in in_all:
                if char.islower(): 
                    converted_num = ord(char) - 96
                elif char.isupper():
                    converted_num = ord(char) - 38
            
            print(f"{converted_num = }")
            print() 
            sum_for_all_groups += converted_num
            
    print(sum_for_all_groups)

if __name__ == "__main__":
    main()