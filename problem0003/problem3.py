import math

def primeFactorCheck(num):
    primeFactors = []

    while num % 2 == 0:
        primeFactors.append(2)
        num = num / 2

    for i in range(3, int(math.sqrt(num))+1,2):
        while num % i == 0:
            primeFactors.append(int(i))
            num = num / i

    if num > 2:
        primeFactors.append(int(num))

    return primeFactors

primeArray = primeFactorCheck(600851475143)

print(primeArray[-1])