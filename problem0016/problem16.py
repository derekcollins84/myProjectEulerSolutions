'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
sumOfDigits = 0
number = (2 ** 1000)

for digit in range(len(str(number))):
    sumOfDigits += int(str(number)[digit])
print(sumOfDigits)
