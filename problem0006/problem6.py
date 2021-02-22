def sumOfSquares(num):
    answer = 0
    for x in range(1, (num + 1)):
        y = x ** 2
        answer = answer + y
    return answer

def squareSum(num):
    y = 0
    for x in range(1,(num + 1)):
        y = y + x
    answer = y ** 2
    return answer

print(squareSum(100) - sumOfSquares(100))