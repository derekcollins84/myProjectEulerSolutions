returnedValues = []
sumOfReturnedValues = 0

for testNum in range(1,1000):
    if testNum % 3 == 0 or \
    testNum % 5 == 0:
        returnedValues.append(testNum)

for x in range(len(returnedValues)):
    sumOfReturnedValues = \
        sumOfReturnedValues \
        + returnedValues[x]

print(sumOfReturnedValues)