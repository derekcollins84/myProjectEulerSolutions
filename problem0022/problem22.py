'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
import csv

nameArray = []
sortedNameArray = []
nameValue = 0
runningTotal = 0

with open('problem0022/p022_names.txt') as csvfile:
    names = csv.reader(csvfile, delimiter=',')
    for line in names:
        for name in line:
            nameArray.append(name)

for name in sorted(nameArray):
    sortedNameArray.append(name)

for namePosition in range(len(sortedNameArray)):
    for i in range(len(sortedNameArray[namePosition])):
        nameValue += ord(sortedNameArray[namePosition][i]) - 64
    nameValue = nameValue * (namePosition + 1)
    runningTotal += nameValue
    nameValue = 0

print(runningTotal)
