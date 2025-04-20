# Milestone 01
# Ask the user to input their weight on Earth
earth_weight = float(input("Enter a weight on Earth: "))

# Mars gravity is 37.8% of Earth's gravity
mars_weight = earth_weight * 0.378

# Round the result to 2 decimal places
rounded_weight = round(mars_weight, 2)

# Display the result
print("The equivalent on Mars:", rounded_weight)


# Milestone 02
# Prompt the user to enter a planet name (must be capitalized correctly)
planet = input("Enter a planet: ")

# Dictionary mapping planets to gravity ratios
gravity_factors = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Calculate the weight based on the selected planet
if planet in gravity_factors:
    planetary_weight = earth_weight * gravity_factors[planet]
    rounded_weight = round(planetary_weight, 2)
    print(f"The equivalent weight on {planet}: {rounded_weight}")
else:
    print("Invalid planet name.")
