f = open("input.txt", "r")

## Copy input as a matrix:
data=[]

for line in f:
    data.append(line)


def part1(arg):

    gamma_rate = findMostUsed(arg)
    gamma_rate_int = int(gamma_rate, 2)

    opposite = { '0':'1', '1':'0'}

    epsilon_rate = (''.join([opposite[b] for b in gamma_rate]))

    epsilon_rate_int = int(epsilon_rate, 2)

    print(f'Final answer is: {epsilon_rate_int * gamma_rate_int}')

    return gamma_rate, epsilon_rate


def part2(arg):

    oxygen = findLast('m',arg)
    c02 = findLast('l', arg)

    oxygen_rate = int(oxygen, 2)
    c02_rate = int(c02, 2)
    print(f"Final final is : {oxygen_rate * c02_rate}")

    
def findMostUsed(arg):
    mostUsed = []
    for position in range(len(arg[0])-1):
        recurrence = 0
        for bit in arg:
            if bit[position] == "0":
                recurrence -=1
            else:
                recurrence +=1
        
        if recurrence >= 0:
            mostUsed.append(1)
        else:
            mostUsed.append(0)

    mostUsed = ''.join(map(str,mostUsed))
    return mostUsed

def findLeastUsed(arg):
    leastUsed = []
    for position in range(len(arg[0])-1):
        recurrence = 0
        for bit in arg:
            if bit[position] == "0":
                recurrence -=1
            else:
                recurrence +=1
        
        if recurrence >= 0:
            leastUsed.append(0)
        else:
            leastUsed.append(1)

    leastUsed = ''.join(map(str,leastUsed))
    return leastUsed

def findLast(aim, data):
    data_copy = data

    position = 0

    while len(data_copy) > 1:
        if aim == 'm':
            toCompare = findMostUsed(data_copy)
        else:
            toCompare = findLeastUsed(data_copy)
        print(toCompare)
        
        tmp =[]
        for binary in data_copy:
            if toCompare[position] == binary[position]:
                print(position, toCompare[position], binary)
                tmp.append(binary)
                
        data_copy = tmp
        position += 1
    
    print("Valeur de base:" + toCompare)
    print("Bit trouvé:" + data_copy[0])

    return data_copy[0]


## Select function here :
part2(data)

## PYTHON EST PAS FOUTU DE POUVOIR VIRER TOUTES LES OCCURENCES D'ELEMENTS DANS UNE LISTE !!!!!