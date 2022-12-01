#! /usr/bin/env python3

def main():
    file = open('input.txt', 'r')
    final_floor = 0
    char_count = 0
    
    while 1:
        char = file.read(1)
        if not char:
            break
        
        char_count += 1
        
        if char == '(':
            final_floor += 1
        if char == ')':
            final_floor -= 1
        if final_floor == -1:
            print(f"{char_count =}")
        # print(char)
    print(f"{final_floor = }")



if __name__ == "__main__":
    main()