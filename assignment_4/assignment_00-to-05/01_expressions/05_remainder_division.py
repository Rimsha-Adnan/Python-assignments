def main():
    # Ask the user to enter the first number
    num1 = int(input("Please enter an integer to be divided: "))

    # Ask the user to enter the second number
    num2 = int(input("Please enter an integer to divide by: "))

    # Calculate the result and remainder
    result = num1 // num2     # Integer division
    remainder = num1 % num2   # Remainder

    # Show the output
    print("The result of this division is", result, "with a remainder of", remainder)

# This line is required to call the main function
if __name__ == '__main__':
    main()
