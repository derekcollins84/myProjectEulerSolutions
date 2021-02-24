'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import time

startTime = time.process_time()
primeArray = [2]
sumOfPrimes = 2


def primeCheck(num):
    for prime in primeArray:
        if num % prime == 0:
            return False
        if prime > int(num ** 0.5) + 1:
            break
    return True


for i in range(3, 2000000, 2):
    if primeCheck(i):
        sumOfPrimes += i
        primeArray.append(i)

print(sumOfPrimes)
print(round(time.process_time() - startTime, 2), "seconds")
