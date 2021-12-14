with open("res/14_input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = """NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C""".splitlines()


def parsePolymer(lines):
    return lines[0]

def parseRules(lines):
    rules = {}
    for line in lines:
        rule = line.split(" -> ")
        rules[rule[0]] = rule[1]
    return rules

def parseInput(lines):
    index = lines.index("")
    polymer = parsePolymer(lines[:index])
    rules = parseRules(lines[index+1:])
    return polymer, rules

def apply(rules, polymer):
    result = ""
    for i in range(0, len(polymer)-1):
        result += polymer[i] + rules[polymer[i:i+2]]
    result += polymer[len(polymer)-1]
    return result

def countChars(polymer):
    counts = {}
    for c in polymer:
        if c not in counts: counts[c] = 0
        counts[c] += 1
    return counts


polymer, rules = parseInput(lines)

for i in range(0, 10):
    polymer = apply(rules, polymer)
charCounts = countChars(polymer)

answer = max(charCounts.values()) - min(charCounts.values())

print(answer)
