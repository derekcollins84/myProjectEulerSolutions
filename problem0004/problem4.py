largestPalindrome = 0

def palindromeCheck(num):
    strNum = str(num)

    if strNum == strNum[::-1]:
        return True

for x in range(999,100,-1):
    for y in range(999,100,-1):
        z = x * y
        if palindromeCheck(z):
            if z > largestPalindrome:
                largestPalindrome = z
                  
print(largestPalindrome)