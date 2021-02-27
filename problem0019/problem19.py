'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
dayOfWeek = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday', 7:'Sunday'}

months = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'June',7:'Jul',8:'Aug',9:'Sept',10:'Oct',11:'Nov',12:'Dec'}

daysInMonthNonLeapYear = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

daysInMonthLeapYear = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

dayCounter = 0
total = 0

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True
    else:
        return False


for year in range(1900, 2001):
    if isLeapYear(year):
        for month in months:
            for day in range(1,daysInMonthLeapYear[month] + 1):
                dayCounter += 1
                if day == 1 and dayCounter == 7 and year > 1900:
                    total += 1
                    print(months[month], day, year, dayOfWeek[dayCounter])
                if dayCounter == 7:
                    dayCounter = 0
    else:
        for month in months:
            for day in range(1,daysInMonthNonLeapYear[month] + 1):
                dayCounter += 1
                if day == 1 and dayCounter == 7 and year > 1900:
                    total += 1
                    print(months[month], day, year, dayOfWeek[dayCounter])
                if dayCounter == 7:
                    dayCounter = 0
print(total)