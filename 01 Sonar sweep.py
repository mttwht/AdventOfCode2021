file = open("res/01_input.txt", "r")

measurements = []
for line in file:
    measurements.append(int(line))

previousMeasurement = None
increases = decreases = 0
windowMeasurements = []

for measurement in measurements:
    windowMeasurements.append(measurement)
    if len(windowMeasurements) > 3:
        windowMeasurements.pop(0)
    if len(windowMeasurements) < 3:
        continue

    measurement = sum(windowMeasurements)
    
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
