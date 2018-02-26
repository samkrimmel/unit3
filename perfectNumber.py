#Sam Krimmel
#2/26/18
#perfectNumber.py - tells whether an entered number is perfect or not

num = int(input('Enter a number: '))

total = 0

for i in range(1,num):
    if num%i == 0:
        total += i

if total == num:
    print('Perfect!')
else:
    print('Not perfect...')
