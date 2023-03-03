#!/usr/bin/env python3

def main():
    with open ("sample.txt") as file:
        lines = file.readlines()
    
    for line in lines:
        print(int(line, 2))

if __name__ == "__main__":
    main()