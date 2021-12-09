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


riskLevelSum = 0
for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        if isLowPoint(lines, x, y):
            riskLevelSum += int(lines[y][x]) + 1

print(riskLevelSum)
