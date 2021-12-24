f = open("input.txt", "r")

def transform_data(arg):
    fold_instructions = []
    dots = []
    jmax= 0
    imax= 0
    for line in arg:
        if line.startswith("fold"):
            fold, along, equation = line.strip().split()
            orientation, index = equation.split('=')
            fold_instructions.append([orientation, index])
        elif line == "\n":
            pass
        else:
            # index i and j are reversed, because i means row, and j means column
            j, i = line.strip().split(',')
            if int(i) > imax :
                imax = int(i)
            if int(j) > jmax :
                jmax = int(j)

            dots.append([int(i),int(j)])
    return dots, fold_instructions, imax, jmax

def fill_paper(paper,dots):
    for dot in dots:
        paper[dot[0]][dot[1]] = '#'
    return paper

def foldup(paper, index_line):
    paper_up = paper[:index_line]
    paper_down = paper[index_line+1:]
    paper_down = paper_down[::-1]
    for i in range(len(paper_up) - len(paper_down),len(paper_down)):
        for j in range(len(paper_down[0])):
            if paper_down[i - (len(paper_up) - len(paper_down))][j] == '#':
                
                paper_up[i][j] = '#'
    return paper_up

def foldside(paper, index_column):
    paper_left = []
    paper_right = []
    for line in paper:
        paper_left.append(line[:index_column])
        right_part = line[index_column+1:]
        paper_right.append(right_part[::-1])

    for i in range(len(paper_right)):
        for j in range(len(paper_left[0]) - len(paper_right[0]), len(paper_right[0])):
            if paper_right[i][j] == '#':
                paper_left[i][j] = '#'

    return paper_left

def count_paper(paper):
    count = 0
    for line in paper:
        count += line.count('#')
    return count

def part1(arg):
    i = 0
    dots, fold_instructions, imax, jmax = transform_data(arg)
    paper = [['_' for x in range(jmax + 1)] for y in range(imax + 1)]
    paper = fill_paper(paper,dots)
    fold = fold_instructions[0]
    if fold[0] == 'y':
        paper = foldup(paper, int(fold[1]))
    else:
        paper = foldside(paper, int(fold[1]))

    return count_paper(paper)

def part2(arg):
    dots, fold_instructions, imax, jmax = transform_data(arg)
    paper = [['_' for x in range(jmax + 1)] for y in range(imax + 1)]
    paper = fill_paper(paper,dots)
    for fold in fold_instructions:
        print(len(paper),len(paper[0]))
        if fold[0] == 'y':
            paper = foldup(paper, int(fold[1]))
        else:
            paper = foldside(paper, int(fold[1]))

    for line in paper:
        print("".join(line))

    return count_paper(paper)


 

## Select function here :
print(part2(f))

