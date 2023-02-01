#!/usr/bin/env python3

def display_matrix(matrix: list) -> None:
    for row in matrix:
        print(row)
    print()
    
def count_light(matrix: list) -> int:
    return sum(sum(row) for row in matrix)

def main():
    matrix = [[0 for j in range(1000)] for i in range(1000)]
    
    with open("input.txt") as f: # automatically closes file
        lines = f.read().split('\n')
    
    for line in lines:
        newline = line.split()
        from_row, from_col = map(int, newline[-3].split(","))        
        to_row, to_col = map(int, newline[-1].split(","))
        
        for row in range(from_row, to_row + 1):
            for col in range(from_col, to_col + 1):
        
                if newline[1] == 'on':                    
                    matrix[row][col] += 1
                    
                elif newline[1] == 'off':
                    if matrix[row][col] != 0:
                        matrix[row][col] -= 1                        
                
                else:
                    matrix[row][col] += 2


    print(f"part 2 = {sum(sum(row) for row in matrix)}")
       


if __name__ == "__main__":
    main()