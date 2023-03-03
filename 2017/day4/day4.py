#!/usr/bin/env python3

def valid_passphrase(line: str) -> bool:
    line = line.split()
    original_len = len(line)
    new_set = set()
    for idx in range(0, len(line)):
        new_set.add(line[idx])

    if original_len == len(new_set):
        return True
    else:
        return False

def valid_passphrase_part2(line: str)  -> bool:
    line = line.split()
    for idx in range(0, len(line)):
        
        print(f"\n\n{line[idx] = }")

        for sidx in range(0, len(line)):
            if idx == sidx:
                continue
            else:
                if sorted(line[idx]) == sorted(line[sidx]):
                    return False
    print("valid")
    return True


def main():
    with open("input.txt") as file:
        lines = file.readlines()
    
    total_valid = 0

    # for line in lines:
        # print(line,end="")
        # if valid_passphrase(line):
        #     total_valid += 1
    
    # print(f"part 1: {total_valid}")

    for line in lines:
        if valid_passphrase_part2(line):
            total_valid += 1

    print(f"\npart 2: {total_valid}")

if __name__=="__main__":
    main()