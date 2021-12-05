import copy

f = open("input.txt", "r")

def transform_data(file):
    # Get incoming inputs
    incoming = f.readline().split(',')
    incoming = list(map(int, incoming))
    

    # Get all boards
    boards = []
    marked_boards = []
    lines = f.readlines()

    count = 0
    board = []
    marked_board = []

    for line in lines:

        if count != 0:
            numeric_line = line.split()
            numeric_line = list(map(int, numeric_line))
            board.append(numeric_line)
            marked_board.append([0]*len(numeric_line))
            if count == 5:
                count = -1
                boards.append(board)
                marked_boards.append(marked_board)
                board = []
                marked_board = []
        count +=1
    
    return incoming, boards, marked_boards
        
def isWinner(marked_board):
    # Row Search:
    for i in range(len(marked_board[0])):
        answer = True
        for line in marked_board:
            # Line Search:
            if sum(line) == 5:
                return True

            if line[i] != 1:
                answer = False

        if answer == True:
            return True

    return False

def isInBoard(number, board):
    position = [0,0]
    i = 0
    for line in board:
        if number in line:
            j = line.index(number)
            position = [i,j]
            return True, position
        i += 1
    return False , position

def sumUnmarked(marked_board, board):
    summ = 0
    for i in range(len(marked_board)):
        for j in range(len(marked_board[0])):
            if marked_board[i][j] == 0:
                summ += board[i][j]
    return summ



def part1(arg):
    incoming, boards, marked_boards = transform_data(arg)

    for number in incoming :
        for board in boards:
            isIn, position = isInBoard(number, board)
            i = boards.index(board)
            if isIn:
                marked_boards[i][position[0]][position[1]] = 1

            if isWinner(marked_boards[i]):
                sumRemain = sumUnmarked(marked_boards[i], board)
                result = sumRemain * number
                return result
 

def part2(arg):
    incoming, boards, marked_boards = transform_data(arg)

    for number in incoming :
        for board in boards:
            isIn, position = isInBoard(number, board)
            i = boards.index(board)
            if isIn:
                marked_boards[i][position[0]][position[1]] = 1

            if isWinner(marked_boards[i]):
                del boards[i]
                del marked_boards[i]

            if len(boards) == 1:
                isIn, position = isInBoard(number, boards[0])
                if isIn:
                    marked_boards[0][position[0]][position[1]] = 1

                print(marked_boards[0],boards[0])
                sumRemain = sumUnmarked(marked_boards[0], boards[0])
                print(sumRemain, number)
                result = sumRemain * number
                return result

def part2_alternative(arg):
    incoming, boards, marked_boards = transform_data(arg)

    last = 0
    summToRemind = 0

    for board in boards:
        marked_board = copy.deepcopy(marked_boards[0])
        i = 0
        for number in incoming: 
            isIn, position = isInBoard(number, board)
            if isIn:
                marked_board[position[0]][position[1]] = 1

            if isWinner(marked_board):
                sumRemain = sumUnmarked(marked_board, board)
                if i > last:
                    summToRemind = sumRemain
                    last = i
                    boardToRemind = board
                break

            i += 1
    return incoming[last] * summToRemind
            
    
 

## Select function here :
print(part2_alternative(f))

