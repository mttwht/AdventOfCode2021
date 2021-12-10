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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def lineScore(line):
    openChunks = []
    for c in line:
        if openings.count(c):
            openChunks.append(c)
        elif c == pairs[openChunks[-1]]:
            openChunks.pop()
        else:
            return points[c]
            
score = 0
for line in lines:
    score += lineScore(line) or 0

print(score)
