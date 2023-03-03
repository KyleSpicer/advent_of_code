#!/usr/bin/env python3

# part one
# def valid_password(line: list) -> bool:
#     first = line.split(":")
#     letter = first[0][-1]
#     password = first[1].strip()
#     range = first[0].split(" ")
#     range = range[0].split("-")
#     i = int(range[0])
#     j = int(range[1])

#     letter_count = password.count(letter)
    
#     if i <= letter_count <= j:
#         return True
#     return False


# part 2
def valid_password(line: list) -> bool:
    first = line.split(":")
    letter = first[0][-1]
    password = first[1].strip()
    range = first[0].split(" ")
    range = range[0].split("-")
    i = int(range[0])
    i = i -1
    j = int(range[1])
    j = j - 1
    
    if password[i] == letter or password[j] == letter:
        if password[j] == password[i]:
            return False
        return True
    

def main():
    with open("input.txt") as file:
        lines = file.readlines()
    
    lines = [line.strip() for line in lines]

    valid_passwords = 0

    for line in lines:
        if valid_password(line):
            valid_passwords += 1
    
    print(f"{valid_passwords = }")
        

if __name__=="__main__":
    main()