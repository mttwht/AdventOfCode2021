with open("res/17_input.txt", "r") as file:
    inputData = file.readline().strip()

# sample data
# inputData = "target area: x=20..30, y=-10..-5" # max-Y = 45


def parseTarget(inputData):
    data = inputData[13:]
    [x,y] = [d[2:] for d in data.split(", ")]
    [xmin,xmax] = [int(v) for v in x.split("..")]
    [ymin,ymax] = [int(v) for v in y.split("..")]
    return ((xmin,xmax), (ymin, ymax))

def doStep(pos, velocity):
    px = pos[0] + velocity[0]
    py = pos[1] + velocity[1]
    vx = 0 if velocity[0] <= 0 else velocity[0] - 1
    vy = velocity[1] - 1
    return (px, py), (vx, vy)

def isInTarget(pos, target):
    if target[0][0] <= pos[0] and pos[0] <= target[0][1]:
        if target[1][0] <= pos[1] and pos[1] <= target[1][1]:
            return True
    return False

def hasMissedTarget(pos, velocity, target):
    # Overshot the mark
    if pos[0] > target[0][1]:
        return True
    # Undershot the mark
    elif pos[1] < target[1][0] and velocity[1] <= 0:
        return True
    else:
        return False

def moveProbe(pos, velocity, target):
    pos, velocity = doStep(pos, velocity)
    
    if hasMissedTarget(pos, velocity, target):
        return None
    elif isInTarget(pos, target):
        return pos
    else:
        return moveProbe(pos, velocity, target)

def fireProbe(velocity, target):
    return moveProbe((0,0), velocity, target)

def calcMaxTravel(velocity):
    return sum(range(velocity+1))

def getMinX(target):
    for x in range(1, target[0][1]):
        if calcMaxTravel(x) >= target[0][0]:
            return x

def getMaxX(target):
    return target[0][1]

def getMinY(target):
    if target[1][0] > 0:
        for y in range(1, target[1][1]):
            if calcMaxTravel(y) >= target[1][0]:
                return y
    else:
        return target[1][0]

def getMaxY(target):
    if target[1][0] >= 0:
        return target[1][1]
    elif target[1][1] <= 0:
        return abs(target[1][0])-1
    else:
        return max(target[1][1], abs(target[1][0])-1)


target = parseTarget(inputData)

for y in range(getMaxY(target), getMinY(target)-1, -1):
    for x in range(getMinX(target), getMaxX(target)+1):
        posInTarget = fireProbe((x,y), target)
        if posInTarget is not None:
            print(calcMaxTravel(y))
            exit()
