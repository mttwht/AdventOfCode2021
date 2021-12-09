with open("res/09_input.txt", "r") as file:
    lines = file.readlines()

# lines = [
#     "2199943210\n",
#     "3987894921\n",
#     "9856789892\n",
#     "8767896789\n",
#     "9899965678\n"
# ]

lines = [x.strip() for x in lines]


def isLowPoint(lines, x, y):
    val = lines[y][x]
    if x > 0 and lines[y][x-1] <= val: return False
    if y > 0 and lines[y-1][x] <= val: return False
    if x < len(lines[y])-1 and lines[y][x+1] <= val: return False
    if y < len(lines)-1 and lines[y+1][x] <= val: return False
    return True

def calculateBasin(lines, x, y, basinArea):
    val = lines[y][x]
    
    if val == '9': return basinArea
    if basinArea.count((x, y)): return basinArea
    
    basinArea.append((x, y))
    
    if x > 0 and lines[y][x-1] > val: basinArea = calculateBasin(lines, x-1, y, basinArea)
    if y > 0 and lines[y-1][x] > val: basinArea = calculateBasin(lines, x, y-1, basinArea)
    if x < len(lines[y])-1 and lines[y][x+1] > val: basinArea = calculateBasin(lines, x+1, y, basinArea)
    if y < len(lines)-1 and lines[y+1][x] > val: basinArea = calculateBasin(lines, x, y+1, basinArea)
    return basinArea

lowPoints = []
for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        if isLowPoint(lines, x, y):
            lowPoints.append((x, y))

basins = []
for low in lowPoints:
    basins.append(calculateBasin(lines, low[0], low[1], []))

basinSizes = [len(b) for b in basins]
basinSizes.sort()

print(basinSizes.pop() * basinSizes.pop() * basinSizes.pop())
