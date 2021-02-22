'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
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