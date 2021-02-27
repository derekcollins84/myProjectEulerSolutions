'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
amicableArray = []


def isAmicable(a):
    dofa = 1
    dofb = 1
    for i in range(2, int(a / 2)+1):
        if a % i == 0:
            dofa += i
    for i in range(2, dofa):
        if dofa % i == 0:
            dofb += i
    if dofb == a and dofa != dofb:
        amicableArray.append(a)
        return True


for testNum in range(1, 10001):
    isAmicable(testNum)
print(sum(amicableArray))
