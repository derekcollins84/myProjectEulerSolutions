'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
largestPalindrome = 0


def palindromeCheck(num):
    strNum = str(num)

    if strNum == strNum(: : -1]:
        return True


for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        z = x * y
        if palindromeCheck(z):
            if z > largestPalindrome:
                largestPalindrome = z

print(largestPalindrome)
