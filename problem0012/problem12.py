'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
import time

startTime = time.process_time()
numArray = [1]
arrayPosition = 0
count = 2


def findDivisors(num):
    divisorsArray = []
    for i in range(1, int(num ** 0.5)):
        if num % i == 0:
            divisorsArray.append(i)
            divisorsArray.append(int(num / i))
    return len(divisorsArray)


while findDivisors(numArray[-1]) < 500:
    numArray.append(numArray[arrayPosition]+count)
    arrayPosition += 1
    count += 1

print(numArray[-1])
print(round(time.process_time() - startTime, 2), "seconds")
