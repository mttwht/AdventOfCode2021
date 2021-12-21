with open("res/20_input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

# #..#.
# #....
# ##..#
# ..#..
# ..###""".splitlines()


# def parseAlgo(algoLine):
#     return [1 if c=='#' else 0 for c in algoLine]

# def parseImage(imageLines):
#     return [[1 if c=='#' else 0 for c in line] for line in imageLines]

def extendImage(image, char=''):
    c = image[0][0] if char=='' else char
    newImage = []
    newImage.append(''.join(c for i in range(len(image)+4)))
    newImage.append(''.join(c for i in range(len(image)+4)))
    for line in image:
        newImage.append(c+c + line + c+c)
    newImage.append(''.join(c for i in range(len(image)+4)))
    newImage.append(''.join(c for i in range(len(image)+4)))
    return newImage

def enhanceImage(image, algo):
    image = extendImage(image)
    outputImage = []
    
    for y in range(1,len(image)-1):
        line = str()
        for x in range(1,len(image[y])-1):
            index = image[y-1][x-1:x+2] + image[y][x-1:x+2] + image[y+1][x-1:x+2]
            index = index.translate(index.maketrans({'.':'0', '#':'1'}))
            index = int(index, 2)
            line += algo[index]
        outputImage.append(line)
    return outputImage

def printImage(image):
    for row in image:
        print(row)

def parseInput(inputLines):
    algo = inputLines[0]
    image = inputLines[2:]
    # algo = parseAlgo(inputLines[0])
    # image = parseImage(inputLines[2:])
    return algo,image

def countPixels(image):
    return sum([row.count('#') for row in image])


algo,image = parseInput(lines)
image = extendImage(image, '.')
printImage(image)
for i in range(2):
    image = enhanceImage(image, algo)
    print()
    printImage(image)

print(countPixels(image))
