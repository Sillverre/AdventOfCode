f = open("example.txt", "r")

def transform_data(arg):
    map_cave = []
    for line in arg:
        map_cave.append(list(map(int,line.strip())))

    return map_cave

def init_map(height, width):
    length_map = [[10000000 for i in range(width)]for j in range(height)]

    length_map[0][0] = 0

    return length_map

def part1(arg):
    map_cave = transform_data(arg)
    length_map = init_map(len(map_cave), len(map_cave[0]))
    path = []
    
    print(length_map)
    return 0

def part2(arg):
    i=0
 

## Select function here :
print(part1(f))

