with open("res/12_input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [
# 	# # sample input 1
# 	# "start-A",
#     # "start-b",
#     # "A-c",
#     # "A-b",
#     # "b-d",
#     # "A-end",
#     # "b-end"
    
#     # # sample input 2
#     # "dc-end",
#     # "HN-start",
#     # "start-kj",
#     # "dc-start",
#     # "dc-HN",
#     # "LN-dc",
#     # "HN-end",
#     # "kj-sa",
#     # "kj-HN",
#     # "kj-dc"
    
#     # # sample input 3
#     # "fs-end",
#     # "he-DX",
#     # "fs-he",
#     # "start-DX",
#     # "pj-DX",
#     # "end-zg",
#     # "zg-sl",
#     # "zg-pj",
#     # "pj-he",
#     # "RW-he",
#     # "fs-DX",
#     # "pj-RW",
#     # "zg-RW",
#     # "start-pj",
#     # "he-WI",
#     # "zg-he",
#     # "pj-fs",
#     # "start-RW"
# ]


def parseInput(input):
    caveMap = {}
    for line in input:
        rooms = line.split("-")
        for room in rooms:
            if room not in caveMap:
                caveMap[room] = []
            caveMap[room].extend(filter(lambda x: x != room, rooms))
    return caveMap

def findPathsTo(map, currentPath, end):
    currentPos = currentPath[len(currentPath)-1]
    
    if currentPos == end:
        return [currentPath]
    elif currentPos.islower() and currentPath.count(currentPos) > 1:
        return None
    
    paths = None
    for room in map[currentPos]:
        tempPath = currentPath.copy()
        tempPath.append(room)
        newPaths = findPathsTo(map, tempPath, end)
        if newPaths is not None:
            if paths is None: paths = []
            paths.extend(newPaths)
    
    return paths
    

caveMap = parseInput(lines)
paths = findPathsTo(caveMap, ["start"], "end")

for path in paths:
    print(path)

print(len(paths))
