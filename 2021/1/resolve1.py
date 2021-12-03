f = open("input.txt", "r")

def part1(arg):
    depths=[]

    for line in arg:
        depths.append(int(line))

    count = 0

    measurements = []

    for i in range(1,len(depths)):
        if int(depths[i]) > int(depths[i-1]):
            print(str(depths[i]) + " contre " + str(depths[i-1]))
            count+=1

    print(count)



def part2(arg):
    depths=[]

    for line in arg:
        depths.append(line)

    count = 0

    measurements = []

    for i in range(len(depths)):
        if i + 2 < len(depths):
            measure = int(depths[i]) + int(depths[i+1]) + int(depths[i+2])
            measurements.append(measure)


    for i in range(1,len(measurements)):
        if measurements[i] > measurements[i-1]:
            print(str(measurements[i]) + " contre " + str(measurements[i-1]))
            count+=1

    print(count)


## Select function here :
part1(f)




## Optimized Solution from https://www.reddit.com/r/adventofcode/comments/r66vow/comment/hmzvzvs/?utm_source=share&utm_medium=web2x&context=3 :
#data = [int(x) for x in open("data\\01.txt", "r")]
#print("Part 1:", sum([data[i] > data[i-1] for i in range(1, len(data))]))
#print("Part 2:", sum([data[i] > data[i-3] for i in range(3, len(data))]))