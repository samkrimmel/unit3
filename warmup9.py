#Sam Krimmel
#3/1/18
#warmup9.py - asks user to input some text and prints it with vowels capitalized

text = input('Enter text: ')

for ch in text:
    ch = ch.lower()
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print(ch.upper())
    else:
        print(ch.lower())
