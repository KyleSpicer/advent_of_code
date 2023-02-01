#!/usr/bin/env python3

def create_bs_matrix() -> list:
        #     1
        #   2 3 4
        # 5 6 7 8 9
        #   A B C
        #     D
        
    matrix = [[0 for _ in range(5)] for _ in range(5)]
    matrix[0][2] = 1
    matrix[1][1] = 2
    matrix[1][2] = 3
    matrix[1][3] = 4
    matrix[2][0] = 5
    matrix[2][1] = 6
    matrix[2][2] = 7
    matrix[2][3] = 8
    matrix[2][4] = 9
    matrix[3][1] = 'A'
    matrix[3][2] = 'B'
    matrix[3][3] = 'C'
    matrix[4][2] = 'D'
    
    return matrix


def display_matrix(matrix: list) -> None:
    for row in matrix:
        print(row)
    print()

def main():
    with open("input.txt") as f:
        lines = f.readlines()
    
    ############################## PART 1 #####################################
    # create / populate matrix
    # count = 1
    # matrix = [[0 for _ in range(3)] for _ in range(3)]
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         matrix[i][j] = count
    #         count += 1
    
    # display_matrix(matrix)
    
    # position_row = 1
    # position_col = 1
    # bathroom_code = []
    # for line in lines:
    #     line = line.replace("\n", "")
    #     for letter in line:
    #         if letter == 'U':
    #             if position_row > 0:
    #                 position_row -= 1
    #         elif letter == 'D':
    #             if position_row < 2:
    #                 position_row += 1
    #         elif letter == 'L':
    #             if position_col > 0:
    #                 position_col -= 1
    #         elif letter == 'R':
    #             if position_col < 2:
    #                 position_col += 1
        
    #     digit = matrix[position_row][position_col]
    #     bathroom_code.append(digit)
        
    
    # print("Part 1: ", end ="")
    # for thing in bathroom_code:
    #     print(thing, end='')
    # print()  
    ############################## PART 1 #####################################
    
    
    ############################## PART 2 #####################################
    
    position_row = 2
    position_col = 0
    bathroom_code = []

    matrix2 = create_bs_matrix()
    display_matrix(matrix2)
    print(matrix2[position_row][position_col])
    
    for line in lines:
        line = line.replace("\n", "")
        for letter in line:
            if letter == 'U':
                if position_row > 0 and (matrix2[position_row - 1][position_col] != 0):
                    position_row -= 1
            elif letter == 'D':
                if position_row < 4 and (matrix2[position_row + 1][position_col] != 0):
                    position_row += 1
            elif letter == 'L':
                if position_col > 0 and (matrix2[position_row][position_col - 1] != 0):
                    position_col -= 1
            elif letter == 'R':
                if position_col < 4 and (matrix2[position_row][position_col + 1] != 0):
                    position_col += 1

        
        digit = matrix2[position_row][position_col]
        bathroom_code.append(digit)
        
    
    print("Part 2: ", end ="")
    for thing in bathroom_code:
        print(thing, end='')
    print()  
    ############################## PART 2 #####################################
    
        
        
        

if __name__ == "__main__":
    main()