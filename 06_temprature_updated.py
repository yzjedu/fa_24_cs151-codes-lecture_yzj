def tell_temp(temp):
    if temp >= 90:
        print('Temperature is too hot.')
    elif temp < 30:
        print('Temperature is tooooooooooo cold')
    else:
        print('Temperature is ok.')

def main():
    print('This program tells you if the temperature is too hot')
    temp = float(input('Enter the temperature in degrees Fahrenheit: '))
    tell_temp(temp)

if __name__ == '__main__':
    main()