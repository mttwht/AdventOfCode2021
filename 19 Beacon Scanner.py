with open("res/19_input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]


def parseInput(lines):
    # store as list so we can use index to identify them
    scanners = list()
    start,end = 0,0
    for i in range(len(lines)):
        line = lines[i]
        if line != "": continue
        end = i
        scanners.append(parseScanner(lines[start:end]))
        start = end+1
    return scanners
def parseScanner(lines):
    # store as set as each point is unique and unordered
    return set(parseBeacon(line) for line in lines[1:])
def parseBeacon(line):
    # store as tuple for ordering and immutability
    return tuple(int(v) for v in line.split(","))

def rotateX(beacon):
    (x,y,z) = beacon
    return (x, z * -1, y)
def rotateY(beacon):
    (x,y,z) = beacon
    return (z, y, x * -1)
def rotateZ(beacon):
    (x, y, z) = beacon
    return (y * -1, x, z)

def rotatePointsX(scanner):
    return [rotateX(beacon) for beacon in scanner]
def rotatePointsY(scanner):
    return [rotateY(beacon) for beacon in scanner]
def rotatePointsZ(scanner):
    return [rotateZ(beacon) for beacon in scanner]
    

def mapPointsOntoFullMap(scanner, fullMap):
    for xy in range(6):
        for z in range(4):
            for (bx,by,bz) in scanner: # b for beacon
                for (rx,ry,rz) in fullMap: # r for reference point
                    (vx,vy,vz) = (rx-bx, ry-by, rz-bz) # v for vector
                    tempMapping = {(tx+vx,ty+vy,tz+vz) for (tx,ty,tz) in scanner} # t for temp
                    if len(fullMap.intersection(tempMapping)) >= 12:
                        return tempMapping
            scanner = rotatePointsZ(scanner)
        scanner = rotatePointsX(scanner) if xy % 2 else rotatePointsY(scanner)



scanners = parseInput(lines)
total = len(scanners)
current = 1

fullMap = scanners.pop(0)

while len(scanners) > 0:
    scanner = scanners.pop(0)
    
    points = mapPointsOntoFullMap(scanner, fullMap)
    
    if points is None:
        scanners.append(scanner)
        print("skip")
    else:
        fullMap = fullMap.union(points)
        current += 1
        print("done", current, "/", total)
	
print(len(fullMap))