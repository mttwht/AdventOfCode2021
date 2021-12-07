with open("res/07_input.txt", "r") as file:
    lines = file.readlines()

crabs = [int(x) for x in lines[0].split(",")]

def triangle(x):
    return x * (x + 1) // 2

energies = []
for i in range(0, max(crabs)+1):
    energies.append(sum([triangle(abs(x - i)) for x in crabs]))

cheapest = min(energies)
print(energies.index(cheapest), ":", cheapest)
