with open("res/21_input.txt", "r") as file:
    lines = [line.strip() for line in file]

# lines = """Player 1 starting position: 4
# Player 2 starting position: 8""".splitlines()

board = list(range(1, 10+1))
rollFreqs = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}


def parseInput(lines):
    playerPositions = {}
    for line in lines:
        words = line.split()
        player = int(words[1])
        position = int(words[4])
        playerPositions[player] = position-1
    return playerPositions

cache = {}
def playGame(players, positions, scores, roll=0):
    wins = dict.fromkeys(players, 0)
    if roll > 0:
        player = players.pop(0)
        players.append(player)
        positions[player] += roll
        positions[player] %= len(board)
        scores[player] += board[positions[player]]
        if scores[player] >= 21:
            wins[player] += 1
            return wins
    
    for roll,freq in rollFreqs.items():
        state = (positions[1], positions[2], scores[1], scores[2], roll, players[1])
        if state in cache:
            results = cache[state]
        else:
            results = playGame(players.copy(), positions.copy(), scores.copy(), roll).items()
            cache[state] = results
        for p,w in results:
            wins[p] += w * freq
    return wins
        


positions = parseInput(lines)
players = list(positions.keys())
scores = dict.fromkeys(players, 0)

outcomes = playGame(players, positions, scores)

for player in players:
    print("player", player, "wins in", outcomes[player], "universes")
