'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''
dictionary = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
              6: 'six', 7: "seven", 8: "eight", 9: 'nine', 10: 'ten', 11: 'eleven',
              12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
              16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
              20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
              70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'onehundred',
              200: 'twohundred', 300: 'threehundred', 400: 'fourhundred',
              500: 'fivehundred', 600: 'sixhundred', 700: 'sevenhundred',
              800: 'eighthundred', 900: 'ninehundred', 1000: 'onethousand'}

total = 0


def numToText(num):

    if num in dictionary:
        return dictionary[num]

    elif len(str(num)) == 2:
        firstDigit = int(str(num)[0]) * 10
        secondDigit = int(str(num)[1])
        return dictionary[firstDigit] + dictionary[secondDigit]

    elif len(str(num)) == 3:
        firstDigit = int(str(num)[0]) * 100

        if str(num)[1] == '0':
            thirdDigit = int(str(num)[2])
            return dictionary[firstDigit] + 'and' + dictionary[thirdDigit]

        elif str(num)[1] == '1' or str(num)[2] == '0':
            endNumber = int(str(num)[1]+str(num)[2])
            return dictionary[firstDigit] + 'and' + dictionary[endNumber]

        elif str(num)[1] in ['2', '3', '4', '5', '6', '7', '8', '9']:
            secondDigit = int(str(num)[1]) * 10
            thirdDigit = int(str(num)[2])
            return dictionary[firstDigit] + 'and' + dictionary[secondDigit] + dictionary[thirdDigit]


for i in range(1, 1001):
    total += len(numToText(i))
    print(numToText(i))
    print(total)
