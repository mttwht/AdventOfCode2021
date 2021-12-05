with open("res/05_input.txt", "r") as file:
    lines = file.readlines()

def parsePoint(str):
    return tuple([int(x) for x in str.split(",")])

def parseVent(line):
    return tuple([parsePoint(x) for x in line.split(" -> ")])

def parseVents(lines):
    return [parseVent(line) for line in lines]
        

vents = parseVents(lines)

diagram = [[0 for j in range(1, 1000)] for i in range(1, 1000)]
for vent in vents:
    # Filter all non-horizontal and non-vertical vents
    if vent[0][0] != vent[1][0] and vent[0][1] != vent[1][1]:
        continue
    
    x = min(vent[0][0], vent[1][0])
    y = min(vent[0][1], vent[1][1])
    
    diagram[x][y] += 1

    while max(vent[0][0], vent[1][0]) > x or max(vent[0][1], vent[1][1]) > y:
        if max(vent[0][0], vent[1][0]) > x:
            x += 1
        elif max(vent[0][1], vent[1][1]) > y:
            y += 1

        diagram[x][y] += 1

crossPoints = 0
for i in range(0, len(diagram)-1):
    for j in range(0, len(diagram[i])-1):
        if diagram[i][j] > 1:
            crossPoints += 1

print(crossPoints)
