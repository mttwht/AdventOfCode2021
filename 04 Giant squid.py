with open("res/04_input.txt", "r") as file:
    lines = file.readlines()

def parseDraws(line):
    return [int(x) for x in line.split(",")]

def parseBoardLine(line):
    return [(int(x), 0) for x in line.split()]

def parseBoard(lines):
    return [parseBoardLine(line) for line in lines]

def parseBoards(lines):
    boards = []
    i = 0
    while i < len(lines):
        boards.append(parseBoard(lines[i:i+5]))
        i += 6
    return boards

def markBoardLine(line, drawNumber):
    return [(x[0], x[1] + int(x[0]==drawNumber)) for x in line]

def markBoard(board, drawNumber):
    return [markBoardLine(line, drawNumber) for line in board]

def markBoards(boards, drawNumber):
    return [markBoard(board, drawNumber) for board in boards]

def isWinningRow(row):
    return sum([x[1] for x in row]) == len(row)

def transpose(list2D):
    transposed_tuples = list(zip(*list2D))
    return [list(sublist) for sublist in transposed_tuples]


def isWinningBoard(board):
    for row in board:
        if isWinningRow(row):
            return True
    for column in transpose(board):
        if isWinningRow(column):
            return True
    return False

def findWinningBoards(boards):
    return [board for board in boards if isWinningBoard(board)]

def getLineScore(line):
    return sum([x[0] for x in line if x[1] == 0])

def getBoardScore(board):
    return sum([getLineScore(line) for line in board])

def getWinningScore(board, number):
    return getBoardScore(board) * number


numberDraws = parseDraws(lines[0])
boards = parseBoards(lines[2:])

for drawNumber in numberDraws:
    boards = markBoards(boards, drawNumber)
    
    winningBoards = findWinningBoards(boards)
    boards = [board for board in boards if not winningBoards.__contains__(board)]
    if len(winningBoards) > 0:
        for board in winningBoards:
            print(board)
            print("score", getWinningScore(board, drawNumber))
