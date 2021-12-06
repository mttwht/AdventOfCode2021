with open("res/06_input.txt", "r") as file:
    lines = file.readlines()

def parseFish(str):
    return [int(x) for x in str.split(",")]

fish = parseFish(lines[0])

for day in range(0, 80):
    print("day", day)
    # age fish by 1 day
    fish = [x - 1 for x in fish]
    # create new fish
    fish.extend(8 for x in fish if x < 0)
    # reset fish which have duplicated
    for i in range(0, len(fish)):
        if fish[i] < 0:
            fish[i] = 6

print(len(fish))
