with open("res/08_input.txt", "r") as file:
    lines = file.readlines()

# # test data
# lines = [
# 	"be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
# 	"edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
# 	"fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
# 	"fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
# 	"aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
# 	"fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
# 	"dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
# 	"bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
# 	"egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
# 	"gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
# ]

def parseLine(line):
    (inputs, outputs) = line.split("|")
    return (inputs.split(), outputs.split())

def sharedSegments(a, b):
    return len([x for x in a if b.count(x)])


parsedLines = [parseLine(line) for line in lines]

answer = 0
for line in parsedLines:
    inputs = line[0]
    vals = list()
    
    one = [v for v in inputs if len(v) == 2][0]
    inputs.remove(one)
    four = [v for v in inputs if len(v) == 4][0]
    inputs.remove(four)
    seven = [v for v in inputs if len(v) == 3][0]
    inputs.remove(seven)
    eight = [v for v in inputs if len(v) == 7][0]
    inputs.remove(eight)
    three = [v for v in inputs if len(v) == 5 and sharedSegments(one, v) == 2][0]
    inputs.remove(three)
    six = [v for v in inputs if len(v) == 6 and sharedSegments(one, v) == 1][0]
    inputs.remove(six)
    nine = [v for v in inputs if len(v) == 6 and sharedSegments(three, v) == 5][0]
    inputs.remove(nine)
    five = [v for v in inputs if len(v) == 5 and sharedSegments(four, v) == 3][0]
    inputs.remove(five)
    zero = [v for v in inputs if len(v) == 6][0]
    inputs.remove(zero)
    two = inputs[0]
    inputs.remove(two)
    
    inputs = [zero, one, two, three, four, five, six, seven, eight, nine]
    
    outputs = ""
    for output in line[1]:
        matches = filter(lambda x: len(x) == len(output) and sharedSegments(x, output) == len(x), inputs)
        outputs += str(inputs.index(list(matches)[0]))
    answer += int(outputs)
    
print(answer)