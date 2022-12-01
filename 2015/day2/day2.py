#! /usr/bin/env python3

def main():
    file = open('input.txt', 'r')
    
    sq_ft_wrapping = 0
    total_wrapping = 0
    
    for line in file:
        line = line.split('x')
        
        
        length = int(line[0])
        width = int(line[1])
        height = int(line[2])
        
        new = [length, width, height]
        new.sort()
        print(new)
        ribbon = new[0] + new[0] + new[1] + new[1]
        
        side1 = length*width
        side2 = width*height
        side3 = height*length
        
        total_before_extra = 2*(length*width) + 2*(width*height) + 2*(height*length)
        
        # get smallest size
        minimum = side1
        if side2 < minimum:
            minimum = side2
        if side3 < minimum:
            minimum = side3
        
        ribbon_wrap = length * width * height
        
        print(f"{ribbon = }")
        print(f"{ribbon_wrap = }")
        total = ribbon + ribbon_wrap
        total_wrapping += total
        
    print(total_wrapping)
            
    

if __name__ == "__main__":
    main()