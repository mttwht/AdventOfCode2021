file = open("res/02_input.txt", "r")

steps = file.readlines()

x = y = aim = 0

for step in steps:
    (command, distance) = step.split()
    if command == "up":
        aim -= int(distance)
    elif command == "forward":
        x += int(distance)
        y += aim * int(distance)
    elif command == "down":
        aim += int(distance)

print("Travelled", x, "forward and", y, "down")
print("Answer", x*y)