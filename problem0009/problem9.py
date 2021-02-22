def tripletCheck(a,b,c):
    return a**2 + b**2 == c**2

def getAnswer():
    for a in range(1, 1000):
        for b in range(a+1,1000):
            c = 1000 - b - a
            if b > c:
                break
            if tripletCheck(a,b,c):
                answer = [a,b,c]
                return a * b * c
                
print(getAnswer())