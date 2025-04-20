import random  # Import the random module to simulate dice rolls

# Number of sides on each die to roll
NUM_SIDES: int = 6

def main():
    # Simulate rolling the first die (random number between 1 and 6)
    die1 = random.randint(1, NUM_SIDES)
    # Simulate rolling the second die (random number between 1 and 6)
    die2 = random.randint(1, NUM_SIDES)

    print("Dice have", NUM_SIDES, "sides each.")
    print("First die rolled:", die1)
    print("Second die rolled:", die2)

    # Calculate the total
    total = die1 + die2
    print("Total of two dice:", total)

# This line is required to call the main() function
if __name__ == '__main__':
    main()
