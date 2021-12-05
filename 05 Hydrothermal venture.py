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
    x,y = vent[0]
    x2,y2 = vent[1]
    
    diagram[x][y] += 1

    while x != x2 or y != y2:
        if x2 > x:
            x += 1
        elif x2 < x:
            x -= 1
            
        if y2 > y:
            y += 1
        elif y2 < y:
            y -= 1

        diagram[x][y] += 1

crossPoints = 0
for i in range(0, len(diagram)-1):
    for j in range(0, len(diagram[i])-1):
        if diagram[i][j] > 1:
            crossPoints += 1

print(crossPoints)
