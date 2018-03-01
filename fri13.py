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
    if day >= 13:  #If the 13th of the month has already passed
        if weekday(year,month,13) == 4:   #If the current day is the 13th
            print(month,"/",13,"/",year)
            frinum += 1
        else:
            while month <= 12:
                if weekday(year,month,13) == 4:
                    print(month,"/",13,"/",year)
                    frinum += 1
                else:
                    month += 1
    else:
        while month <= 12:
                if weekday(year,month,13) == 4:
                    print(month,"/",13,"/",year)
                    frinum += 1
                else:
                    month += 1