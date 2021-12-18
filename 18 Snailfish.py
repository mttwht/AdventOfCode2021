with open("res/18_input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

lines = """[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]""".splitlines()

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

def sfNeedsExploding(n, depth=1):
    return False

def sfDoExplode(n):
    return n

def sfNeedsSplitting(n):
    return False

def sfDoSplit(n):
    return n

def sfReduce(n):
    processing = True
    while processing:
        if sfNeedsExploding(n):
            n = sfDoExplode(n)
        elif sfNeedsSplitting(n):
            n = sfDoSplit(n)
        else:
            processing = False
    return n

def sfAdd(n1, n2):
    result = [n1, n2]
    result = sfReduce(result)
    return result


sfNumbers = []
for line in lines:
    n,s = parseSfNumber(line)
    sfNumbers.append(n)

result = None
for n in sfNumbers:
    print(n)
    if result is None:
        result = n
    else:
        result = sfAdd(result, n)

print(result)
