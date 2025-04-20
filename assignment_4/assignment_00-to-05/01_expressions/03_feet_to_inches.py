def main():
    # Ask the user to enter number in feet
    feet = float(input("Enter number in feet: "))

    # Convert feet to inches (1 foot = 12 inches)
    inches = feet * 12

    # Print the result
    print(f" That is {inches} inches!")

# This provided line is required to run the program
if __name__ == '__main__':
    main()
