# Speed of light in meters per second
C: int = 299_792_458

def main():

    # Ask the user for mass in kilograms
    mass = float(input("Enter kilos of mass: "))

    # Calculate energy using the formula E = m * c^2
    energy = mass * (C ** 2)

    # Print results in a readable way
    print("\ne = m * C^2...")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s")
    print(f"{energy} joules of energy!")

if __name__ == '__main__':
    main()
