def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))  # Get the initial value from the user
    
    # Keep doubling the value while it's less than 100
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")

if __name__ == '__main__':
    main()
