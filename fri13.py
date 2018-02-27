#Sam Krimmel
#2/26/18
#fri13.py - prints the next ten friday the 13ths

from calendar import weekday
from datetime import date

year = date.today().year
month = date.today().month
day = date.today().day

frinum = 0

while frinum < 10:
    if weekday() == 4 and day == 13:
        print(month/day/year)
        frinum += 1

    if date.today().day > 13:
        if weekday(year,month,13) == 4:
            print(month,"/",13,"/",year)
