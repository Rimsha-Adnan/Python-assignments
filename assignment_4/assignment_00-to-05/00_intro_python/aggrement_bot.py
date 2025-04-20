# 🐾 This program asks the user for their favorite animal
# and replies with the same animal in a friendly sentence.


def main():
    # Ask the user for their favorite animal
    favorite_animal = input("What's your favorite animal? ")

    # Respond using the user's input
    print("My favorite animal is also", favorite_animal + "!")

# Call the main function
if __name__ == '__main__':
    main()
