fibSequence =[1,2]
currentPosition = 0
newNumber = 0
runningTotal = 0

while newNumber <= 4000000:
    newNumber =\
        (fibSequence[currentPosition]+\
            fibSequence[currentPosition + 1])
    if newNumber >= 4000000:
        break
    fibSequence.append(newNumber)
    currentPosition += 1

for x in range(len(fibSequence)):
    if fibSequence[x] % 2 == 0:
        runningTotal += fibSequence[x]

print(runningTotal)