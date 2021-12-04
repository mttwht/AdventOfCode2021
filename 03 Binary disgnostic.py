with open("res/03_input.txt", "r") as file:
    lines = file.readlines()

oxygenGeneratorRatingLines = lines.copy()
co2ScrubberRatingLines = lines.copy()

for i in range(0, len(lines[0])-1):
    zeroes = ones = 0
    for line in oxygenGeneratorRatingLines:
        zeroes += 1 - int(line[i])
        ones += int(line[i])
    if ones >= zeroes:
        temp = filter(lambda x: x[i] == '1', oxygenGeneratorRatingLines)
    else:
        temp = filter(lambda x: x[i] == '0', oxygenGeneratorRatingLines)
    oxygenGeneratorRatingLines = list(temp)
        
    if len(oxygenGeneratorRatingLines) == 1:
        break

oxygenGeneratorRating = oxygenGeneratorRatingLines[0][:-1]

for i in range(0, len(lines[0])-1):
    zeroes = ones = 0
    for line in co2ScrubberRatingLines:
        zeroes += 1 - int(line[i])
        ones += int(line[i])
    if ones >= zeroes:
        temp = filter(lambda x: x[i] == '0', co2ScrubberRatingLines)
    else:
        temp = filter(lambda x: x[i] == '1', co2ScrubberRatingLines)
    co2ScrubberRatingLines = list(temp)
        
    if len(co2ScrubberRatingLines) == 1:
        break

co2ScrubberRating = co2ScrubberRatingLines[0][:-1]

print('oxygenGeneratorRating =', oxygenGeneratorRating, '=', int(oxygenGeneratorRating, 2))
print('co2ScrubberRating =', co2ScrubberRating, '=', int(co2ScrubberRating, 2))

print(int(oxygenGeneratorRating, 2) * int(co2ScrubberRating, 2))
