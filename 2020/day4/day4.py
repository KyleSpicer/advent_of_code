#!/usr/bin/env python3
def valid_byr(value) -> bool:
    if len(value) != 4:
        return False
    
    if not (1920 <= int(value) <= 2002):
        return False
    
    else:
        return True

def valid_iyr(value) -> bool:
    if len(value) != 4:
        return False
    if not (2010 <= int(value) <= 2020):
        return False
    else:
        return True

def valid_eyr(value) -> bool:
    if len(value) != 4:
        return False
    if not (2020 <= int(value) <= 2030):
        return False
    else:
        return True
    
def valid_height(value) -> bool:
    last_two = value[-2:]
    actual_nums = value[:-2]
    if last_two == 'cm' or last_two == 'in':
        if actual_nums.isdigit():
            if last_two == 'cm':
                if 150 <= int(actual_nums) <= 193:
                    return True
                else:
                    return False
            elif last_two == 'in':
                if 59 <= int(actual_nums) <= 76:
                    return True
                else:
                    return False
    return False

def valid_hcl(value) -> bool:    
    if value[0] != '#':
        return False

    valid_chars = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for letter in value[1:]:
        if letter not in valid_chars:
            return False

    return True

def valid_ecl(value) -> bool:
    valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return value in valid

def valid_pid(value) -> bool:
    if len(value) != 9 or not int(value):
        return False
    return True

def validate_input(batch: dict) -> bool:
    # print(batch)

    birth_year = batch.get('byr')
    if not valid_byr(birth_year):
        return False

    issue_year = batch.get('iyr')
    if not valid_iyr(issue_year):
        return False

    expiration_year = batch.get('eyr')
    if not valid_eyr(expiration_year):
        return False
        
    height = batch.get('hgt')
    if not valid_height(height):
        return False

    hair_color = batch.get('hcl')
    if not valid_hcl(hair_color):
        return False

    eye_color = batch.get('ecl')
    if not valid_ecl(eye_color):
        return False

    pass_id = batch.get('pid')
    if not valid_pid(pass_id):
        return False

    return True

def valid_passport(line: str) -> bool:
    data = {
        'byr': None,
        'iyr': None,
        'eyr': None,
        'hgt': None,
        'hcl': None,
        'ecl': None,
        'pid': None
    }

    cutup = line.split(" ")
    for thing in cutup:
        thing = thing.split(":")
        if thing[0] in data.keys():
            data[thing[0]] = thing[1]

    any_none_values = any(value is None for value in data.values())
    if any_none_values:
        return False
    else:
        if validate_input(data):
            return True
        return False


def main():

    batches = []

    with open("input.txt") as file:
        lines = file.readlines()

        catted_string = ""
        for line in lines:
            if line != "\n":
                line = line.strip()
                catted_string += " " + ''.join(line)

            else:
                batches.append(catted_string)
                catted_string = ""

        if catted_string:
            batches.append(catted_string)

    valid_count = 0

    for batch in batches:
        if valid_passport(batch):
            valid_count += 1

    print(f"part two = {valid_count}")


if __name__ == "__main__":
    main()
