with open("res/16_input.txt", "r") as file:
    line = file.readline().strip()

# line =  "C200B40A82" # 1 + 2 = 3
# line =  "04005AC33890" # 6 * 9 = 54
# line =  "880086C3E88112" # min(7,8,9) = 7
# line =  "CE00C43D881120" # max(7,8,9) = 9
# line =  "D8005AC2A8F0" # 5 < 15 = 1
# line =  "F600BC2D8F" # 5 > 15 = 0
# line =  "9C005AC2F8F0" # 5 == 15 = 0
# line =  "9C0141080250320F1802104A08" # 1 + 3 == 2 * 2 = 1

LITERAL_TYPE = 4

OPERATOR_SUM = 0
OPERATOR_PRODUCT = 1
OPERATOR_MIN = 2
OPERATOR_MAX = 3
OPERATOR_GREATERTHAN = 5
OPERATOR_LESSTHAN = 6
OPERATOR_EQUALTO = 7

SUB_PACKET_LENGTH_TYPE = 0
SUB_PACKET_NUMBER_TYPE = 1


def hexStrToBinStr(s):
    binStr = ""
    for c in s:
        i = int(c, 16)
        b = bin(i)[2:]
        binStr += b.zfill(4)
    return binStr

def getVersion(stream):
    version = int(stream[0:3], 2)
    return version

def getType(stream):
    return int(stream[3:6], 2)

def parseLiteral(stream):
    result = ""
    c,stream = stream[:6],stream[6:]
    packet = c
    processing = True
    while processing:
        group,stream = stream[:5],stream[5:]
        packet += group
        result += group[1:]
        if group[0] == '0':
            processing = False
    return packet, int(result, 2)

def getLengthTypeId(stream):
    b = stream[6]
    return int(b, 2)

def getSubPacketLength(stream):
    b = stream[7:][:15]
    return int(b, 2)

def getSubPacketNumber(stream):
    b = stream[7:][:11]
    return int(b, 2)

def parseOperator(stream):
    lengthTypeId = getLengthTypeId(stream)
    
    vals = []
    
    if lengthTypeId == SUB_PACKET_LENGTH_TYPE:
        length = getSubPacketLength(stream)
        totalPacketBitLength = 7 + 15 + length
        subPacket = stream[7+15:totalPacketBitLength]
        while len(subPacket) > 0:
            p,v = parseLiteral(subPacket) if getType(subPacket)==LITERAL_TYPE else parseOperator(subPacket)
            subPacket = subPacket[len(p):]
            vals.append(v)
        packet = stream[:totalPacketBitLength]
    elif lengthTypeId == SUB_PACKET_NUMBER_TYPE:
        number = getSubPacketNumber(stream)
        subPacket = stream[7+11:]
        packet = stream[:7+11]
        for i in range(number):
            p,v = parseLiteral(subPacket) if getType(subPacket)==LITERAL_TYPE else parseOperator(subPacket)
            packet += p
            subPacket = subPacket[len(p):]
            vals.append(v)
    
    operator = getType(packet)
    if operator == OPERATOR_SUM: val = sum(vals)
    elif operator == OPERATOR_PRODUCT:
        val = vals[0]
        for i in range(1, len(vals)): val *= vals[i]
    elif operator == OPERATOR_MIN: val = min(vals)
    elif operator == OPERATOR_MAX: val = max(vals)
    elif operator == OPERATOR_GREATERTHAN: val = 1 if vals[0] > vals[1] else 0
    elif operator == OPERATOR_LESSTHAN: val = 1 if vals[0] < vals[1] else 0
    elif operator == OPERATOR_EQUALTO: val = 1 if vals[0] == vals[1] else 0
    
    return packet, val


def getPacket(stream):
    packetType = getType(stream)
    
    if packetType == LITERAL_TYPE:
        packet, val = parseLiteral(stream)
    else:
        packet, val = parseOperator(stream)
        
    return packet, val

def hexPadPacket(packet, stream):
    # clean up any incomplete hex characters
    while len(packet) % 4:
        packet += stream[len(packet)]
    # Remove trailing zeros
    while stream[len(packet):len(packet)+4] == "0000":
        packet += stream[len(packet):len(packet)+4]
    return packet


inputStream = hexStrToBinStr(line)

totalVersion = 0
while len(inputStream) > 0:
    packet,val = getPacket(inputStream)
    packet = hexPadPacket(packet,inputStream)
    inputStream = inputStream[len(packet):]
    print("{0}\t{1}".format(hex(int(packet, 2)), val))
