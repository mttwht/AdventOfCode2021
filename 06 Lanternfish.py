with open("res/06_input.txt", "r") as file:
    lines = file.readlines()

def parseFish(str):
    return [int(x) for x in str.split(",")]

fish = parseFish(lines[0])
fishCounts = [fish.count(i) for i in range(0, 9)]

for day in range(0, 256):
    # age fish by 1 day
    dupes = fishCounts[0]
    fishCounts = [fishCounts[i+1] for i in range(0, len(fishCounts)-1)]
    # create new fish
    fishCounts.append(dupes)
    # reset fish which have duplicated
    fishCounts[6] += dupes

print(sum(fishCounts))
