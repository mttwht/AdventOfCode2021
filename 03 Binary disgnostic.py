with open("res/03_input.txt", "r") as file:
    lines = file.readlines()

gamma = epsilon = ''

for i in range(0, len(lines[0])-1):
    zeroes = ones = 0
    for line in lines:
        zeroes += 1 - int(line[i])
        ones += int(line[i])
    if ones > zeroes:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
    
print('gamma =', gamma, '=', int(gamma, 2))
print('epsilon =', epsilon, '=', int(epsilon, 2))

print(int(gamma, 2) * int(epsilon, 2))
