import random  # Import the random module

# Constants for the number of random numbers and the range
N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    # Loop to print N_NUMBERS random integers within the range from MIN_VALUE to MAX_VALUE
    for _ in range(N_NUMBERS):  # Repeat the loop N_NUMBERS times
        random_number = random.randint(MIN_VALUE, MAX_VALUE)  # Generate a random number in the given range
        print(random_number, end=" ")  # Print the number on the same line, followed by a space
    
    print()  # Print a newline after all numbers are printed

# This line is required to start the main() function when the program runs
if __name__ == '__main__':
    main()
