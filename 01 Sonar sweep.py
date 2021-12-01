file = open("res/01_input.txt", "r")

measurements = []
for line in file:
    measurements.append(int(line))

previousMeasurement = None
increases = decreases = 0

for measurement in measurements:
    if previousMeasurement is None:
        difference = "N/A - no previous measurement"
    elif measurement > previousMeasurement:
        difference = "increased"
        increases += 1
    else:
        difference = "decreased"
        decreases += 1
        
    print(measurement, "(" + difference + ")")
    previousMeasurement = measurement
    
print(increases, "total increases")
print(decreases, "total decreases")
