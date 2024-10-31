def celsius_to_farhenite(celsius):
    return celsius * 1.8 + 32

def main():
    temperature = float(input("Enter temperature in Celsius: "))
    temperature_far = celsius_to_farhenite(temperature)
    print(f'The temperature in Fahrenheit is: {temperature_far}')

main()