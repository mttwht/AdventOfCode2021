with open("res/08_input.txt", "r") as file:
    lines = file.readlines()


def parseLine(line):
    (inputs, outputs) = line.split("|")
    return (inputs.split(), outputs.split())


parsedLines = [parseLine(line) for line in lines]

hits = 0
for line in parsedLines:
    for value in line[1]:
        if([2,3,4,7].count(len(value))):
            hits += 1

print(hits)
