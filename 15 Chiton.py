with open("res/15_input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

lines = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".splitlines()


def parseMap(lines):
	caveMap = []
	for line in lines:
		caveMap.append([int(x) for x in line])
	return caveMap

def getNorth(caveMap, pos):
    return (pos[0], pos[1]-1) if pos[1] > 0 else None

def getEast(caveMap, pos):
    return (pos[0]+1, pos[1]) if pos[0] < len(caveMap[0])-1 else None

def getSouth(caveMap, pos):
    return (pos[0], pos[1]+1) if pos[1] < len(caveMap)-1 else None

def getWest(caveMap, pos):
    return (pos[0]-1, pos[1]) if pos[0] > 0 else None

def getNeighbours(caveMap, pos):
    return list(filter(None, [
        getNorth(caveMap, pos),
        getEast(caveMap, pos),
        getSouth(caveMap, pos),
        getWest(caveMap, pos)
    ]))

                
def calculateLowestRiskPaths(caveMap):
    riskPaths = [[None for x in row] for row in caveMap]
    emptyNexts = set()
    
    riskPaths[0][0] = 0
    emptyNexts.add((0, 1))
    emptyNexts.add((1, 0))
    
    while len(emptyNexts) > 0:
        lowestNewRisk = lowestNextPos = None
        for next in emptyNexts:
            nextCellVal = caveMap[next[0]][next[1]]
            for neighbour in getNeighbours(caveMap, next):
                nPathRisk = riskPaths[neighbour[0]][neighbour[1]]
                if nPathRisk is None: continue
                if lowestNewRisk is None or nextCellVal + nPathRisk < lowestNewRisk:
                    lowestNewRisk = nextCellVal + nPathRisk
                    lowestNextPos = next
        
        riskPaths[lowestNextPos[0]][lowestNextPos[1]] = lowestNewRisk
        emptyNexts.remove(lowestNextPos)
        for n in getNeighbours(caveMap, lowestNextPos):
            if riskPaths[n[0]][n[1]] is None: emptyNexts.add(n)

    return riskPaths


caveMap = parseMap(lines)
lowestRiskPaths = calculateLowestRiskPaths(caveMap)

risk = lowestRiskPaths[len(caveMap)-1][len(caveMap[len(caveMap)-1])-1]

print(risk)
