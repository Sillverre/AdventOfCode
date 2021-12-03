f = open("input.txt", "r")

def part1(arg):

    depth = 0
    horizontal = 0

    for line in arg:
        direction, value = line.split()
        if direction == "forward":
            horizontal += int(value) 
        elif direction == "up":
            depth -= int(value)
        elif direction == "down":
            depth += int(value)  

    print(f"depth = {depth} , horizontal = {horizontal} , answer = {depth * horizontal} ")

def part2(arg):

    aim = 0
    depth = 0
    horizontal = 0

    for line in arg:
        direction, value = line.split()
        if direction == "forward":
            horizontal += int(value) 
            depth += aim * int(value) 
        elif direction == "up":
            aim -= int(value)
        elif direction == "down":
            aim += int(value)  

    print(f"aim = {aim}, horizontal = {horizontal}, answer = {depth * horizontal}")


## Select function here :
part2(f)