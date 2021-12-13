with open("res/13_input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [
#     "6,10",
#     "0,14",
#     "9,10",
#     "0,3",
#     "10,4",
#     "4,11",
#     "6,0",
#     "6,12",
#     "4,1",
#     "0,13",
#     "10,12",
#     "3,4",
#     "3,0",
#     "8,4",
#     "1,10",
#     "2,14",
#     "8,10",
#     "9,0",
#     "",
#     "fold along y=7",
#     "fold along x=5"
# ]


def parseDots(input):
    return [tuple([int(x) for x in line.split(",")]) for line in input]

def parseFolds(input):
    return [(line[11], int(line[13:])) for line in input]

def parseInput(input):
    index = input.index("")
    dots = parseDots(input[:index])
    folds = parseFolds(input[index+1:])
    return dots, folds

def foldOnX(paper, x):
    foldedPage = [row[0:x] for row in paper]
    for row in range(0, len(foldedPage)):
        for col in range(0, len(foldedPage[row])):
            distFromFold = x - col
            if x + distFromFold < len(paper[row]):
                foldedPage[row][col] += paper[row][x + distFromFold]
    return foldedPage

def foldOnY(paper, y):
    foldedPage = paper[0:y]
    for row in range(0, len(foldedPage)):
        distFromFold = y - row
        for col in range(0, len(foldedPage[row])):
            if y + distFromFold < len(paper):
                foldedPage[row][col] += paper[y + distFromFold][col]
    return foldedPage

def fold(paper, instruction):
    foldMethod = foldOnX if instruction[0] == 'x' else foldOnY
    return foldMethod(paper, instruction[1])

def printPaper(paper):
	for row in paper:
		print(str(map(lambda x: "#" if x else ".", row)))

def countDots(paper):
    return sum([sum([1 for point in row if point > 0]) for row in paper])


dots, folds = parseInput(lines)

maxX = max(map(lambda x: x[0], dots))
maxY = max(map(lambda y: y[1], dots))

paper = [[0 for x in range(0, maxX+1)] for y in range(0, maxY+1)]

for x,y in dots:
    paper[y][x] = 1

for f in folds:
    paper = fold(paper, f)
    print(countDots(paper))
    break
