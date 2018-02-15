#Sam Krimmel
#2/15/18
#gauss.py - adds up all numbers in a range with a difference

low = int(input('Enter the lowest number in the range: '))
high = int(input('Enter the highest number in the range: '))
diff = int(input('Enter a difference: '))
total = 0
for i in range(low,high+1,diff):
    total += i
print('The sum of the numbers from', low,'to', high,'is', total)
