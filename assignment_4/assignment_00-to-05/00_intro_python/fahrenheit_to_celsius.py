# Ask the user to enter the temperature in Fahrenheit
def main():

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius using the formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0

# Show the result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == '__main__':
    main()
