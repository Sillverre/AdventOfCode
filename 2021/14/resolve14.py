f = open("example.txt", "r")

def transform_data(arg):
    template = arg.readline().strip()

    pairs = []
    elements = []
    alphabet = []
    for line in arg.readlines():
        if line != "\n":
            pair, arrow, element = line.strip().split()
            pairs.append(pair)
            elements.append(element)
            if element not in alphabet:
                alphabet.append(element)
    return template, pairs, elements, alphabet


def count_max_min(template, alphabet):
    maxi = 0
    mini = len(template)
    for letter in alphabet:
        occurence = template.count(letter)
        print(letter, "VS", occurence)
        if occurence > maxi:
            maxi = occurence
        if occurence < mini:
            mini = occurence

    return maxi, mini

def part1(arg):
    template, pairs, elements, alphabet = transform_data(arg)
    iteration = 10
    for i in range(iteration):
        j = 0
        while j < len(template) :
            if j == len(template):
                pair = template[j:]
            else:
                pair = template[j:j+2]
            if pair in pairs:
                index = pairs.index(pair)
                template = template[:j+1] + elements[index] +template[j+1:]
                j += 1
            j += 1

    maxi, mini = count_max_min(template, alphabet)
    
    return maxi - mini

def part2(arg):
    template, pairs, elements, alphabet = transform_data(arg)
    iteration = 40
    
 

## Select function here :
print(part1(f))

