
f = open("input.txt", "r")

def add_connection(all_caves, map_connection, cave1, cave2):
    if cave1 not in all_caves:
        all_caves.append(cave1)
        map_connection.append([cave2])
    else:
        map_connection[all_caves.index(cave1)].append(cave2)

    if cave2 not in all_caves:
        all_caves.append(cave2)
        map_connection.append([cave1])
    else:
        map_connection[all_caves.index(cave2)].append(cave1)

    return all_caves, map_connection

def transform_data(arg):
    all_caves = []
    map_connection = []
    for line in arg:
        cave1,cave2 = line.strip().split('-')
        all_caves, map_connection = add_connection(all_caves, map_connection, cave1, cave2)

    return all_caves, map_connection


def explore(current_path, map_path, all_caves, map_connection):
    current_cave = current_path[-1]
    index_current = all_caves.index(current_cave)
    for possible_cave in map_connection[index_current]:
        if possible_cave == "end":
            current_path.append(possible_cave)
            map_path.append(current_path)
            current_path = current_path[:-1]
        elif (possible_cave.islower() and possible_cave != "start" and current_path.count(possible_cave) < 1) or possible_cave.isupper():
            path_copy = current_path[:]
            path_copy.append(possible_cave)
            map_path = explore(path_copy, map_path, all_caves, map_connection)

    return map_path

def check_doubleExplo(possible_cave, current_path):
    for cave in current_path:
        if cave.islower() and cave != "start" and cave != "end":
            if current_path.count(cave) > 1 :
                if cave == possible_cave or current_path.count(possible_cave) > 0:
                    return False
    return True


def explore2(current_path, map_path, all_caves, map_connection):
    current_cave = current_path[-1]
    index_current = all_caves.index(current_cave)
    for possible_cave in map_connection[index_current]:
        if possible_cave == "end":
            current_path.append(possible_cave)
            map_path.append(current_path)
            current_path = current_path[:-1]
        elif (possible_cave.islower() and possible_cave != "start" and check_doubleExplo(possible_cave, current_path)) or possible_cave.isupper():
            path_copy = current_path[:]
            path_copy.append(possible_cave)
            map_path = explore2(path_copy, map_path, all_caves, map_connection)

    return map_path

def part1(arg):
    all_caves, map_connection = transform_data(arg)
    start_path = ["start"]
    map_path = explore(start_path, [], all_caves, map_connection)

    for path in map_path:
        print(path)

    print(len(map_path))


def part2(arg):
    all_caves, map_connection = transform_data(arg)
    start_path = ["start"]
    map_path = explore2(start_path, [], all_caves, map_connection)

    for path in map_path:
        print(path)

    print(len(map_path))
 

## Select function here :
part2(f)

