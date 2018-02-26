#Sam Krimmel
#2/26/18
#divisors.py - asks user for number and prints all divisors

num = int(input('Enter a number: '))

for i in range(1,num):
    if num%i == 0:
        print(i)
    
