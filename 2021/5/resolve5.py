import copy 

f = open("input.txt", "r")

def transform_data(arg):
    start_points = []
    end_points = []

    lines = f.readlines()

    for line in lines:
        start, arrow, end = line.split()
        start_x, start_y = start.split(',')
        end_x, end_y = end.split(',')
        start_points.append([int(start_x), int(start_y)])
        end_points.append([int(end_x), int(end_y)])

    return start_points, end_points

def find_max_array(start_points, end_points):
    all_x = []
    all_y = []
    for point in start_points:
        all_x.append(point[0])
        all_y.append(point[1])
    for point in end_points:
        all_x.append(point[0])
        all_y.append(point[1])

    max_x = max(all_x) + 1
    max_y = max(all_y) + 1

    diagram = [[0 for x in range(max_x)] for y in range(max_y)] 

    return diagram

def check_vertical(start_point, end_point):

    if start_point[0] == end_point[0]:
        return True, start_point[0], start_point[1], end_point[1]
    else:
        return False, 0, 0, 0

def check_horizontal(start_point, end_point):

    if start_point[1] == end_point[1]:
        return True, start_point[1], start_point[0], end_point[0]
    else:
        return False, 0, 0, 0

def check_diagonal(start_point, end_point):
    # Diagonal Type 1: Top left -> bot right
    if (start_point[0] - end_point[0])  == (start_point[1] - end_point[1]):
        return True, 0
    # Diagonal Type 2: Top right -> bot left
    elif (start_point[0] - end_point[0]) == (end_point[1] - start_point[1]):
        return True, 1

    return False, 0
    

def write_vertical(diagram, y, x1, x2):
    if x1 <= x2:
        for x in range(x1, x2 +1):
            diagram[x][y] += 1
    else:
        for x in range(x2, x1 +1):
            diagram[x][y] += 1

    return diagram

def write_horizontal(diagram,  x, y1, y2):

    if y1 <= y2:
        for y in range(y1, y2 +1):
            diagram[x][y] += 1
    else:
        for y in range(y2, y1 +1):
            diagram[x][y] += 1
    
    return diagram

def write_diagonal(diagram,  type, start_point, end_point):
    if type == 0 :
        if start_point[0] < end_point[0]:
            for i in range(end_point[0] - start_point[0] + 1):
                diagram[start_point[1] + i][start_point[0] + i] += 1
        else:
            for i in range(start_point[0] - end_point[0] + 1):
                diagram[end_point[1] + i][end_point[0] + i] += 1
    if type == 1 :
        if start_point[0] < end_point[0]:
            for i in range(end_point[0] - start_point[0] + 1):
                diagram[start_point[1] - i][start_point[0] + i] += 1
            
        else:
            for i in range(start_point[0] - end_point[0] + 1):
                diagram[start_point[1] + i][start_point[0] - i] += 1

    return diagram
        
    
def count_diagram(diagram):
    count = 0
    for x in range(len(diagram)):
        for y in range(len(diagram[0])):
            if diagram[x][y] >1 :
                count += 1
    return count

def diagram_matrix(diagram):
    for line in diagram:
        print(line)

def part1(arg):
    start_points, end_points = transform_data(arg)
    diagram = find_max_array(start_points, end_points)

    for i in range(len(start_points)):

        check, x, y1, y2 = check_vertical(start_points[i], end_points[i])
        if check:
            print("vertical")
            diagram = write_vertical(diagram, x, y1, y2)

        check, y, x1, x2 = check_horizontal(start_points[i], end_points[i])
        if check:
            print("horizontal")
            diagram = write_horizontal(diagram, y, x1, x2)

    print(diagram)
    return count_diagram(diagram) 



def part2(arg):
    start_points, end_points = transform_data(arg)
    diagram = find_max_array(start_points, end_points)

    for i in range(len(start_points)):

        check, x, y1, y2 = check_vertical(start_points[i], end_points[i])
        if check:
            print("vertical")
            diagram = write_vertical(diagram, x, y1, y2)

        check, y, x1, x2 = check_horizontal(start_points[i], end_points[i])
        if check:
            print("horizontal")
            diagram = write_horizontal(diagram, y, x1, x2)

        check, type = check_diagonal(start_points[i], end_points[i])
        if check:
            print("diagonal ", type , start_points[i], end_points[i])
            diagram = write_diagonal(diagram, type, start_points[i], end_points[i])
    
    
    return count_diagram(diagram) 
 

## Select function here :
print(part2(f))

