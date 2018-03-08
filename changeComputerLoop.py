#Sam Krimmel
#3/8/18
#changeComputerLoop.py - asks user for number of cents and outputs change

change = int(input('Enter change in cents: '))

for i in range(1,10):
    quar = cash//25
    dime = (cash - 25*quar)//10
    nick = (cash - (dime*10 + quar*25))//5
    penn = cash - (dime*10 + quar*25 + nick*5)

print('Quarters: ', quar)
print('Dimes: ', dime)
print('Nickels: ', nick)
print('Pennies: ', penn)


