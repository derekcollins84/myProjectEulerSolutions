'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
returnedValues = []
sumOfReturnedValues = 0

for testNum in range(1, 1000):
    if testNum % 3 == 0 or \
            testNum % 5 == 0:
        returnedValues.append(testNum)

for i in range(len(returnedValues)):
    sumOfReturnedValues = \
        sumOfReturnedValues \
        + returnedValues[i]

print(sumOfReturnedValues)
