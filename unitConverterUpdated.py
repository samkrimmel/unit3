#Sam Krimmel
#1/29/18
#unitConverter.py - converts units with four possible conversions

while True:
    print('1) Kilometers to Miles')
    print('2) Kilograms to Pounds')
    print('3) Liters to Gallons')
    print('4) Celsius to Fahrenheit')
    print('5) Quit')

    choice = int(input('Choose your conversion:'))
    
    if choice == 1:
        num = float(input('Enter distance in Kilometers:'))
        print(num, 'Kilometers is', round(num/0.621371,2), 'miles.')
    elif choice == 2:
        num = float(input('Enter weight in Kilograms:'))
        print(num, 'Kilograms is', round(num/2.20462,2), 'pounds.')
    elif choice == 3:
        num = float(input('Enter a volume in liters:'))
        print(num, 'liters is', round(num/0.264172,2), 'gallons.')
    elif choice == 4:
        num = float(input('Enter degrees in Celsius:'))
        print(num, 'degrees Celsius is', round(((num*1.8)+32),2), 'degrees Fahrenheit.')
    elif choice == 5:
        break
    else:
        print('Error!')
