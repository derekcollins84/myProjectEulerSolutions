'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
def findDivisibles(num):
    checkList = [11,13,14,16,17,18,19,20]
    divisibles = [x for x in checkList if num % x == 0]
    return len(divisibles)

startNum = 2520
endNum = 1000000000

for num in range(startNum,endNum,2520):
    if findDivisibles(num) == 8:
        print(num)
        break