f = open("input.txt", "r")

def transform_data(arg):
    array = []
    for line in arg:
        array.append(list(map(int,line.strip())))
    return array

def find_low_points(array):
    risk = 0
    map_low_points = []
    for i in range(len(array)):
        for j in range(len(array[0])):
            is_low = True
            value = array[i][j]
            #Check line conditions
            if i == 0:
                if value >= array[i+1][j]:
                    is_low = False
            elif i == len(array)-1:
                if value >= array[i-1][j]:
                    is_low = False
            else:
                if value >= array[i-1][j] or value >= array[i+1][j]:
                    is_low = False
            
            #Check row conditions
            if j == 0:
                if value >= array[i][j+1]:
                    is_low = False
            elif j == len(array[0])-1:
                if value >= array[i][j-1]:
                    is_low = False
            else:
                if value >= array[i][j+1] or value >= array[i][j-1]:
                    is_low = False

            #Apply results
            if is_low:
                risk += 1 + value
                map_low_points.append([i,j])
    return risk, map_low_points

def explore_position(array,i,j, map_basin):
    value = array[i][j]
    map_basin.append([i,j])
    #Check line conditions
    if i == 0:
        if value < array[i+1][j] and array[i+1][j] < 9 and [i+1,j] not in map_basin:
            map_basin = explore_position(array,i+1,j, map_basin)

    elif i == len(array)-1:
        if value < array[i-1][j] and array[i-1][j] < 9 and [i-1,j] not in map_basin:
            map_basin = explore_position(array,i-1,j, map_basin)

    else:
        if value < array[i+1][j] and array[i+1][j] < 9 and [i+1,j] not in map_basin:
            map_basin = explore_position(array,i+1,j, map_basin)
        if value < array[i-1][j] and array[i-1][j] < 9 and [i-1,j] not in map_basin:
            map_basin = explore_position(array,i-1,j, map_basin)
        
    #Check row conditions
    if j == 0:
        if value < array[i][j+1] and array[i][j+1] < 9 and [i,j+1] not in map_basin:
            map_basin = explore_position(array,i,j+1, map_basin)

    elif j == len(array[0])-1:
        if value < array[i][j-1] and array[i][j-1] < 9 and [i,j-1] not in map_basin:
            map_basin = explore_position(array,i,j-1, map_basin)

    else:
        if value < array[i][j+1] and array[i][j+1] < 9 and [i,j+1] not in map_basin:
            map_basin = explore_position(array,i,j+1, map_basin)
        if value < array[i][j-1] and array[i][j-1] < 9 and [i,j-1] not in map_basin:
            map_basin = explore_position(array,i,j-1, map_basin)
    
    return map_basin

    


def explore_basin(array, map_low_points):
    all_basin_size = []
    all_map_basins = []
    for i,j in map_low_points:
        map_basin = []
        map_basin = explore_position(array,i,j, map_basin)
        all_map_basins.append(map_basin)
        all_basin_size.append(len(map_basin))

    return all_basin_size , all_map_basins

def part1(arg):
    array = transform_data(arg)

    return find_low_points(array)[0]

 

def part2(arg):
    array = transform_data(arg)
    map_low_points = find_low_points(array)[1]

    list_size , all_map_basins = explore_basin(array, map_low_points)

    list_size.sort(reverse = True)
    print(list_size)

    return list_size[0] * list_size[1] * list_size[2]
        

 

## Select function here :
print(part2(f))

