with open("res/11_input.txt", "r") as file:
    lines = [[int(x) for x in line.strip()] for line in file.readlines()]

# lines = [[int(x) for x in line] for line in [
#     "5483143223",
#     "2745854711",
#     "5264556173",
#     "6141336146",
#     "6357385478",
#     "4167524645",
#     "2176841721",
#     "6882881134",
#     "4846848554",
#     "5283751526"
# ]]


def flashOctopus(grid, posX, posY):
    for y in range(max(0, posY-1), min(len(grid), posY+2)):
        for x in range(max(0, posX-1), min(len(grid[y]), posX+2)):
            grid[y][x] += 1
            if grid[y][x] == 10: flashOctopus(grid, x, y)

def doStep(grid):
    # Flash Octopi
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            grid[y][x] += 1
            if grid[y][x] == 10: flashOctopus(grid, x, y)
    # reset tired octopi
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] > 9: grid[y][x] = 0

def countFlashes(grid):
	return sum([sum([1 for x in row if x == 0]) for row in grid])

flashes = 0
for i in range(0, 100):
    doStep(lines)
    flashes += countFlashes(lines)

print(flashes)
