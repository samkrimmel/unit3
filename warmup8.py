#Sam Krimmel
#2/28/18
#warmup8.py - Find sum if all number less than 100,000 that are divisible bu 3, 10 , and 17

sum = 0

for i in range(1,100001):
    if i%3 == 0 and i%10 == 0 and i%17 == 0:
        sum += i

print(sum)
