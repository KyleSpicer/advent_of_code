#!/usr/bin/env python3

def increase_opcode_idx(opcodes: list) -> list:
    new_opcode = []
    for opcode in opcodes:
        new_opcode.append(opcode + 4)

    return new_opcode

def run_program(code, noun, verb):
    code[1] = noun
    code[2] = verb

    opcode_idx = [0,1,2,3]

    while opcode_idx[3] <= len(code):
    
        if code[opcode_idx[0]] == 1:
            # add
            code[code[opcode_idx[3]]] = code[code[opcode_idx[1]]] + code[code[opcode_idx[2]]]
            
        elif code[opcode_idx[0]] == 2:
            # multiply
            code[code[opcode_idx[3]]] = code[code[opcode_idx[1]]] * code[code[opcode_idx[2]]]
        else:
            break

        opcode_idx = increase_opcode_idx(opcode_idx)
    
    return code[0]

def main():
    # opcode one adds
    # opcode two multiplies

    with open("input.txt") as file:
        line = file.readline()
    
    line = line.split(',')
    code = [int(num) for num in line] # converts each item to an int

    
    answer = 19690720
    for i in range(99):
        for j in range(99):
            if run_program(code[:], i, j) == answer:
                print(i, j, answer)
                part_two = (100 * i) + j
                print(part_two)




# PART ONE
    # opcodes are in fours
    # opcode_idx = [0,1,2,3]

    # while opcode_idx[3] <= len(code):
    
    #     if code[opcode_idx[0]] == 1:
    #         # add
    #         code[code[opcode_idx[3]]] = code[code[opcode_idx[1]]] + code[code[opcode_idx[2]]]
            
    #     elif code[opcode_idx[0]] == 2:
    #         # multiply
    #         code[code[opcode_idx[3]]] = code[code[opcode_idx[1]]] * code[code[opcode_idx[2]]]



    #     opcode_idx = increase_opcode_idx(opcode_idx)
    

    # print(f"after:  {code}")
    # part one, change input pos 1,2 to 12, 2
    # print(f"part one = {code[0]}")




    

if __name__=="__main__":
    main()