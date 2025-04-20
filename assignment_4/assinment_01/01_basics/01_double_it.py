def main():
    curr_value = int(input("Enter a number: "))  # Get the user's input
    
    while curr_value < 100:  # Continue doubling the value until it's >= 100
        curr_value = curr_value * 2
        print(curr_value, end=" ")  # Print each doubled value on the same line

if __name__ == '__main__':
    main()
