import math  # Import math module to use math.sqrt()

def main():
    # Ask the user to enter the lengths of sides AB and AC
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Use the Pythagorean theorem to calculate the hypotenuse BC
    bc = math.sqrt(ab**2 + ac**2)

    # Print the result
    print("The length of BC (the hypotenuse) is:", bc)

# This line runs the main() function
if __name__ == '__main__':
    main()
