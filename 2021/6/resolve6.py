def transform_data(arg):
    return list(map(int,f.readline().split(',')))

###########################################################
# This solution will burn your computer faster than an oven
#
def print_fish(fishs, day):
    print("Taille: ", len(fishs)," , Jour: ", day) #, "Liste : ", fishs)
#
#
def advance(fish_list):
    newborn = 0
    
    for i in range(len(fish_list)):
        fish_list[i] -= 1
        if fish_list[i] < 0:
            fish_list[i] = 6
            newborn += 1
    for i in range(newborn):
            fish_list.append(8)
        
    return fish_list
#
###########################################################

def print_fish_value(fishs, day):
    print("Taille: ", sum(fishs)," , Jour: ", day, " , Détail: ", fishs) 

def count_fish(fish_list):
    fish_value = [0]*9
    for fish in fish_list:
        fish_value[fish] += 1

    return fish_value

def advance_evolution(fish_value):
    new_borns = 0
    for i in range(8):
        if i == 0:
            new_borns = fish_value[0]
        fish_value[i] = fish_value[i+1]
    fish_value[6] += new_borns
    fish_value[-1] = new_borns

    return fish_value


def part1(arg):
    fish_list = transform_data(arg)

    fish_value = count_fish(fish_list)
    print_fish_value(fish_value, 0)

    for day in range(1, 81):
        fish_value = advance_evolution(fish_value)
        
        print_fish_value(fish_value, day)

 

def part2(arg):
    fish_list = transform_data(arg)

    fish_value = count_fish(fish_list)
    print_fish_value(fish_value, 0)

    for day in range(1, 257):
        fish_value = advance_evolution(fish_value)
        
        print_fish_value(fish_value, day)

 

## Select function here :
if __name__ == "__main__":
    f = open("input.txt", "r")
    part2(f)



## Optimized solution from https://www.reddit.com/user/JerreST/
# I really like the pop method which avoid a lot of my advance_evolution function

""" 
from year2021.util import read_input

if __name__ == '__main__':
    input = [int(i) for i in read_input('input.txt')[0].split(',')]

    # define initial state of the list
    fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in input:
        fishes[fish] += 1

    # Simulate number of days
    for day in range(256):
        fishes.append(fishes.pop(0))
        fishes[6] += fishes[8]

    print(f"Number of fishes present: {sum(fishes)}")
 """