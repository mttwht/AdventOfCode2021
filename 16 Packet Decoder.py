with open("res/16_input.txt", "r") as file:
    line = file.readline()

# line =  "D2FE28"						# v=6
# line += "38006F45291200"				# v=1
# line += "EE00D40C823060"				# v=7
# line += "8A004A801A8002F478"			# v=16
# line += "620080001611562C8802118E34"	# v=12
# line += "C0015000016115A2E0802F182340"	# v=23
# line += "A0016C880162017C3686B18A3D4780"# v=31

LITERAL_TYPE = 4
SUB_PACKET_LENGTH_TYPE = 0
SUB_PACKET_NUMBER_TYPE = 1


def hexStrToBinStr(s):
    i = int(s, 16)
    b = bin(i)[2:]
    return b.zfill((len(s)-1)*4)

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
    return packet, getVersion(packet)

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
    version = getVersion(stream)
    
    if lengthTypeId == SUB_PACKET_LENGTH_TYPE:
        length = getSubPacketLength(stream)
        totalPacketBitLength = 7 + 15 + length
        subPacket = stream[7+15:totalPacketBitLength]
        while len(subPacket) > 0:
            p,v = parseLiteral(subPacket) if getType(subPacket)==LITERAL_TYPE else parseOperator(subPacket)
            subPacket = subPacket[len(p):]
            version += v
        packet = stream[:totalPacketBitLength]
    elif lengthTypeId == SUB_PACKET_NUMBER_TYPE:
        number = getSubPacketNumber(stream)
        subPacket = stream[7+11:]
        packet = stream[:7+11]
        for i in range(number):
            p,v = parseLiteral(subPacket) if getType(subPacket)==LITERAL_TYPE else parseOperator(subPacket)
            packet += p
            subPacket = subPacket[len(p):]
            version += v
    
    return packet, version
        

def getPacket(stream):
    packetType = getType(stream)
    
    if packetType == LITERAL_TYPE:
        packet, version = parseLiteral(stream)
    else:
        packet, version = parseOperator(stream)
        
    return packet, version

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
    packet,version = getPacket(inputStream)
    packet = hexPadPacket(packet,inputStream)
    inputStream = inputStream[len(packet):]
    totalVersion += version
    print("{0}\t{1}".format(hex(int(packet, 2)), version))

print("totalVersion","=",totalVersion)
