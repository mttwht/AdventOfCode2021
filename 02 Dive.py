file = open("res/02_input.txt", "r")

steps = file.readlines()

x = y = 0

for step in steps:
    (command, distance) = step.split()
    if command == "up":
        y -= int(distance)
    elif command == "forward":
        x += int(distance)
    elif command == "down":
        y += int(distance)

print("Travelled", x, "forward and", y, "down")
print("Answer", x*y)