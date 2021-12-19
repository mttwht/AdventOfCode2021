with open("res/18_input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = """[1,1]
# [2,2]
# [3,3]
# [4,4]""".splitlines()
# # final sum = [[[[1,1],[2,2]],[3,3]],[4,4]]
# # magnitude = 445

# lines = """[1,1]
# [2,2]
# [3,3]
# [4,4]
# [5,5]""".splitlines()
# # final sum = [[[[3,0],[5,3]],[4,4]],[5,5]]
# # magnitude = 791

lines = """[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]""".splitlines()
# final sum = [[[[5,0],[7,4]],[5,5]],[6,6]]
# magnitude = 1137

# lines = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
# [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
# [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
# [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
# [7,[5,[[3,8],[1,4]]]]
# [[2,[2,2]],[8,[8,1]]]
# [2,9]
# [1,[[[9,3],9],[[9,0],[0,7]]]]
# [[[5,[7,4]],7],1]
# [[[[4,2],2],6],[8,7]]""".splitlines()
# # final sum = [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
# # magnitude = 3488

# lines = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# [[[5,[2,8]],4],[5,[[9,9],0]]]
# [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# [[[[5,4],[7,7]],8],[[8,3],8]]
# [[9,3],[[9,9],[6,[4,9]]]]
# [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".splitlines()
# # final sum = [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
# # magnitude = 4140


def strPop(s, i):
    c = s[i]
    s = s[:i] + s[i+1:]
    return s,c

def parseSfNumber(s):
    s,c = strPop(s,0)
    if c == '[':
        n1,s = parseSfNumber(s)
        s,c = strPop(s,0) # pop ,
        n2,s = parseSfNumber(s)
        s,c = strPop(s,0) # pop ]
        return [n1,n2], s
    else:
        n = c
        while s[0] >= '0' and s[0] <= '9':
            s,c = strPop(s,0)
            n += c
        return int(n), s
    
def getPair(s, i):
    lb = s.rindex('[', 0, i+3)
    rb = s.index(']', i)
    return s[lb:rb+1], lb

def getStrint(s, i):
    chars = s[i]
    startPos = i
    for j in range(i-1, 0, -1):
        if s[j] >= '0' and s[j] <= '9':
            chars = s[j] + chars
            startPos = j
        else:
            break
    for j in range(i+1, len(s)):
        if s[j] >= '0' and s[j] <= '9':
            chars = chars + s[j]
        else:
            break
    return chars, startPos

def sfNeedsExploding(n):
    openBrackets = 0
    s = str(n)
    for i in range(len(s)):
        c = s[i]
        if c == '[': openBrackets += 1
        elif c == ']': openBrackets -= 1
        if openBrackets > 4: return i

def sfDoExplode(n):
    s = str(n)
    i = sfNeedsExploding(n)
    pair, iPair = getPair(s, i)
    left, iLeft = getStrint(s, i+1)
    right, iRight = getStrint(s, iPair+len(pair)-2)
    for j in range(iPair+len(pair), len(s)):
        if s[j] >= '0' and s[j] <= '9':
            num, iNum = getStrint(s, j)
            s = s[:iNum] + str(int(num) + int(right)) + s[iNum+len(num):]
            break
    s = s[:iPair] + '0' + s[iPair+len(pair):]
    for j in range(iPair-1, 0, -1):
        if s[j] >= '0' and s[j] <= '9':
            num, iNum = getStrint(s, j)
            s = s[:iNum] + str(int(num) + int(left)) + s[iNum+len(num):]
            break
    s = s.replace(" ", "")
    n,s = parseSfNumber(s)
    return n

def sfNeedsSplitting(n):
    if type(n) == int:
        return True if n >= 10 else False
    else:
        return sfNeedsSplitting(n[0]) or sfNeedsSplitting(n[1])

def sfDoSplit(n):
    if type(n) == int:
        if n >= 10: return [int(n/2), int((n+1)/2)],True
        else: return n,False
    else:
        n0,n0split = sfDoSplit(n[0])
        n[0] = n0
        if n0split: n1,n1split = n[1],False
        else: n1,n1split = sfDoSplit(n[1])
        n[1] = n1
        return n,(n0split or n1split)

def sfReduce(n):
    processing = True
    while processing:
        if sfNeedsExploding(n):
            n = sfDoExplode(n)
        elif sfNeedsSplitting(n):
            n,_ = sfDoSplit(n)
        else:
            processing = False
    return n

def sfAdd(n1, n2):
    result = [n1, n2]
    result = sfReduce(result)
    return result

def sfMagnitude(n):
    if type(n) == int: return n
    else: return 3 * sfMagnitude(n[0]) + 2 * sfMagnitude(n[1])

sfNumbers = []
for line in lines:
    n,s = parseSfNumber(line)
    sfNumbers.append(n)

result = None
for n in sfNumbers:
    if result is None:
        result = n
        print(n)
    else:
        result = sfAdd(result, n)
        print("+", n)
        print("=", result)

print(result)
print(sfMagnitude(result))
