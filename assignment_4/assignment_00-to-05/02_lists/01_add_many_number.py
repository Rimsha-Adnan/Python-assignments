def sum_list(numbers):
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total = sum(numbers)
    return total

def main():
    # Example list of numbers
    numbers = [5, 10, 15, 20]
    
    # Call the function to get the sum
    total = sum_list(numbers)

    # Print the result
    print("The sum of the numbers is:", total)

# This line calls the main function
if __name__ == '__main__':
    main()
