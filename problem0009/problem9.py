'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
def tripletCheck(a,b,c):
    return a**2 + b**2 == c**2

def getAnswer():
    for a in range(1, 1000):
        for b in range(a+1,1000):
            c = 1000 - b - a
            if b > c:
                break
            if tripletCheck(a,b,c):
                return a * b * c
                
print(getAnswer())