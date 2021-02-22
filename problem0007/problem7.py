import math

primeArray = []
x = 2

def primeCheck(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            break
    else:
        return True

while len(primeArray) < 10001:
    if primeCheck(x):
        primeArray.append(x)
    x = x + 1

print(primeArray[-1])
