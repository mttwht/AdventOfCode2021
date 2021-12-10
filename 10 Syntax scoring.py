with open("res/10_input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [
#     "[({(<(())[]>[[{[]{<()<>>",
#     "[(()[<>])]({[<{<<[]>>(",
#     "{([(<{}[<>[]}>{[]{[(<()>",
#     "(((({<>}<{<{<>}{[]{[]{}",
#     "[[<[([]))<([[{}[[()]]]",
#     "[{[{({}]{}}([{[{{{}}([]",
#     "{<[[]]>}<{[{[{[]{()[[[]",
#     "[<(<(<(<{}))><([]([]()",
#     "<{([([[(<>()){}]>(<<{{",
#     "<{([{{}}[<[[[<>{}]]]>[]]"
# ]

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
openings = list(pairs.keys())
closings = list(pairs.values())
points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def lineScore(line):
    openChunks = []
    for c in line:
        if openings.count(c):
            openChunks.append(c)
        elif c == pairs[openChunks[-1]]:
            openChunks.pop()
        else:
            return None
    
    score = 0
    openChunks.reverse()
    for c in openChunks:
        score *= 5
        score += points[pairs[c]]
    return score
            
scores = []
for line in lines:
    score = lineScore(line)
    if score: scores.append(score)

scores.sort()
print(scores[int(len(scores) / 2)])
