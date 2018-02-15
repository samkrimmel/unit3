#Sam Krimmel
#2/15/18
#printStarts.py - prints pyramid of asterisks

num = int(input('Pick a numba: '))

for i in range(1,num):
    print(' '*((num-1)-i),' *'*i)
    
