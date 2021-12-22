with open("res/21_input.txt", "r") as file:
    lines = [line.strip() for line in file]

# lines = """Player 1 starting position: 4
# Player 2 starting position: 8""".splitlines()

board = list(range(1, 10+1))
die = list(range(1,100+1))
rollCounter = 0


def parseInput(lines):
    start1 = int(lines[0].split().pop())
    start2 = int(lines[1].split().pop())
    return board.index(start1), board.index(start2)

def getDieRoll():
    global rollCounter
    val = die[rollCounter % 100]
    rollCounter += 1
    return val


pos1,pos2 = parseInput(lines)
score1 = score2 = 0

while score1 < 1000 and score2 < 1000:
    roll = 0
    for i in range(3): roll += getDieRoll()
    if rollCounter % 2 == 1:
        pos1 += roll
        pos1 %= len(board)
        score1 += board[pos1]
    else:
        pos2 += roll
        pos2 %= len(board)
        score2 += board[pos2]

print("losing score", min(score1,score2))
print("dice rolls", rollCounter)
print("result", min(score1,score2) * rollCounter)