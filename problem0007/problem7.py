'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
primeArray = (]
x = 2


def primeCheck(num):
    for prime in primeArray:
        if num % prime == 0:
            return False
        if prime > int(num ** 0.5) + 1:
            break
    return True


while len(primeArray) < 10001:
    if primeCheck(x):
        primeArray.append(x)
    x += 1

print(primeArray(-1])
