#!/usr/bin/env python3

def p1(data):
    total_possible = 0

    for game in data:
        if p1_process_game(game[1:]):
            total_possible += int(game[0])
    
    return total_possible

def p1_process_game(game):
    max_red = 12
    max_green = 13
    max_blue = 14

    curr_val = 0

    for item in game:
        if item.isdigit():
            curr_val = int(item)
        
        else:
            if "blue" == item:
                if max_blue < curr_val:
                    return False
                
            if "green" == item:
                if max_green < curr_val:
                    return False
                
            if "red" == item:
                if max_red < curr_val:
                    return False
    
    return True

def p2(data):
    total_value = 0

    for game in data:
        total_value += process_p2(game[1:])
    
    return total_value

def process_p2(game):
    max_red = 0
    max_green = 0
    max_blue = 0

    curr_val = 0

    for item in game:
        if item.isdigit():
            curr_val = int(item)
        
        else:
            if item == "red":
                if curr_val > max_red:
                    max_red = curr_val

            if item == "blue":
                if curr_val > max_blue:
                    max_blue = curr_val

            if item == "green":
                if curr_val > max_green:
                    max_green = curr_val

    return max_green * max_red * max_blue

def main():
    with open("input.txt", "r") as file:
        contents = file.readlines()
        contents = [line.strip() for line in contents]
    
    new_data = []
    
    for line in contents:
        line = line[5:]
        line = line.replace(";", "")
        line = line.replace(":", "")
        line = line.replace(",", "")
        line = line.split(" ")
        new_data.append(line)

    p1_answer = p1(new_data)
    print(f"{p1_answer = }")

    p2_answer = p2(new_data)
    print(f"{p2_answer = }")
    

if __name__=="__main__":
    main()