f = open("input.txt", "r")

def transform_data(arg):
    map_octopus = []

    for line in arg:
        line_octopus = list(map(int,list(line.strip())))
        map_octopus.append(line_octopus)
    
    return map_octopus

def increment_map(map_octopus):
    for x in range(len(map_octopus)):
        for y in range(len(map_octopus[0])):
            map_octopus[x][y] += 1
    return map_octopus

def explode(map_octopus, map_flashes, x ,y):
    if x == 0:
        if y == 0:
            map_octopus[x+1][y] += 1
            map_octopus[x+1][y+1] += 1
            map_octopus[x][y+1] += 1

        elif y == len(map_octopus[0])-1:
            map_octopus[x+1][y] += 1
            map_octopus[x+1][y-1] += 1
            map_octopus[x][y-1] += 1
    
        else:
            map_octopus[x+1][y] += 1
            map_octopus[x+1][y+1] += 1
            map_octopus[x][y+1] += 1
            map_octopus[x+1][y-1] += 1
            map_octopus[x][y-1] += 1
        
    elif x == len(map_octopus)-1:
        if y == 0:
            map_octopus[x-1][y] += 1
            map_octopus[x-1][y+1] += 1
            map_octopus[x][y+1] += 1

        elif y == len(map_octopus[0])-1:
            map_octopus[x-1][y] += 1
            map_octopus[x-1][y-1] += 1
            map_octopus[x][y-1] += 1
    
        else:
            map_octopus[x-1][y] += 1
            map_octopus[x-1][y+1] += 1
            map_octopus[x][y+1] += 1
            map_octopus[x-1][y-1] += 1
            map_octopus[x][y-1] += 1
        
    else:
        if y == 0:
            map_octopus[x-1][y] += 1
            map_octopus[x-1][y+1] += 1
            map_octopus[x][y+1] += 1
            map_octopus[x+1][y] += 1
            map_octopus[x+1][y+1] += 1

        elif y == len(map_octopus[0])-1:
            map_octopus[x-1][y] += 1
            map_octopus[x-1][y-1] += 1
            map_octopus[x][y-1] += 1
            map_octopus[x+1][y-1] += 1
            map_octopus[x+1][y] += 1
            
    
        else:
            map_octopus[x-1][y] += 1
            map_octopus[x-1][y+1] += 1
            map_octopus[x-1][y-1] += 1
            map_octopus[x][y+1] += 1
            map_octopus[x][y-1] += 1
            map_octopus[x+1][y] += 1
            map_octopus[x+1][y+1] += 1
            map_octopus[x+1][y-1] += 1
    
    return check_explosion(map_octopus, map_flashes)
            
      
            
                

    

def check_explosion(map_octopus, map_flashes):
    for x in range(len(map_octopus)):
        for y in range(len(map_octopus[0])):
            if map_octopus[x][y] > 9 and map_flashes[x][y] == 0:
                map_flashes[x][y] = 1
                map_octopus, map_flashes = explode(map_octopus, map_flashes, x ,y)

    return map_octopus, map_flashes

def reset_map(map_octopus):
    for x in range(len(map_octopus)):
        for y in range(len(map_octopus[0])):
            if map_octopus[x][y] > 9 :
                map_octopus[x][y] = 0
    return map_octopus

def count_flash(map_flashes):
    count = 0
    for x in map_flashes:
        count += sum(x)
    return count

def part1(arg):
    map_octopus = transform_data(arg)
    final = 100
    flash_count = 0
    for i in range(final):

        map_flashes = [[0 for x in range(len(map_octopus))] for y in range(len(map_octopus[0]))]

        map_octopus = increment_map(map_octopus)

        map_octopus, map_flashes = check_explosion(map_octopus, map_flashes)

        map_octopus = reset_map(map_octopus)

        flash_count += count_flash(map_flashes)
    
    return flash_count
    

def part2(arg):
    map_octopus = transform_data(arg)
    step = 0
    while 1:
        step += 1
        map_flashes = [[0 for x in range(len(map_octopus))] for y in range(len(map_octopus[0]))]

        map_octopus = increment_map(map_octopus)

        map_octopus, map_flashes = check_explosion(map_octopus, map_flashes)

        map_octopus = reset_map(map_octopus)

        if count_flash(map_flashes) == len(map_octopus) * len(map_octopus[0]):
            return step
    
 

## Select function here :
print(part2(f))

