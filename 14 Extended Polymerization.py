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

def apply(rules, pairs):
    result = dict.fromkeys(rules.keys(), 0)
    for k, v in rules.items():
        result[k[0]+v] += pairs[k]
        result[v+k[1]] += pairs[k]
    return result

def countChars(pairs, polymer):
    counts = {}
    for k, v in pairs.items():
        if k[0] not in counts: counts[k[0]] = 0
        counts[k[0]] += v
    counts[polymer[len(polymer)-1]] += 1
    return counts


polymer, rules = parseInput(lines)
pairs = dict.fromkeys(rules.keys(), 0)
for i in range(0, len(polymer)-1): pairs[polymer[i:i+2]] += 1

for i in range(0, 40):
    pairs = apply(rules, pairs)

print(pairs)

charCounts = countChars(pairs, polymer)

answer = max(charCounts.values()) - min(charCounts.values())

print(answer)
