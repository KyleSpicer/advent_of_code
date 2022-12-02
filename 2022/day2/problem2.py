#! /usr/bin/env python3

def main():    
    # outcome of the round: lost = 0, draw = 3, win = 6
    # rock = 1, paper = 2, scissors = 3
    # opponent: a = rock, b = paper, c = scissors
    # you: y = rock, x = paper, z = scissors
    
    opponent_score = 0
    your_score = 0
    round_count = 0
    
    file = open("input.txt", "r")
    lines = file.readlines()
    
    opponent_round_score = 0
    your_round_score = 0
    
    # X = lose
    # Y = draw
    # Z = win
    
    
    for line in lines:
        round_count += 1
        print(f"\n\nRound #: {round_count}")
        print(line, end="\n")
        
        if line[0] == "A" and line[2] == "X":
            # rock, lose, scissors
            your_score += 3 + 0
            
        if line[0] == "A" and line[2] == "Y":
            # rock, draw, rock
            your_score += 1 + 3
            
        if line[0] == "A" and line[2] == "Z":
            # rock, win, paper 
            your_score += 2 + 6
            
            
            
        if line[0] == "B" and line[2] == "X":
            # paper, lose, rock
            your_score += 1 + 0
            
        if line[0] == "B" and line[2] == "Y":
            # paper, draw, paper
            your_score += 2 + 3
            
        if line[0] == "B" and line[2] == "Z":
            # paper, win, scissors
            your_score += 3 + 6
            
            
            
        if line[0] == "C" and line[2] == "X":
            # scissors, lose, paper
            your_score += 2 + 0
            
        if line[0] == "C" and line[2] == "Y":
            # scissors, draw, scissors
            your_score += 3 + 3
            
        if line[0] == "C" and line[2] == "Z":
            # scissors, win, rock
            your_score += 1 + 6
        print(f"{your_score = }")
        
        
            
    print("\nEnd of Game Score:")
    print(f"{your_score = }")
    
            
    print()
    

if __name__ == "__main__":
    main() 