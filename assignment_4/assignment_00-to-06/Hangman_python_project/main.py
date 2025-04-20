import random
import requests
import string

# Define a variable to store the fetched data
word_list = []

def fetch_words():
    url = "https://www.randomlists.com/data/words.json"

    try:
        response = requests.get(url)
        data = response.json()  # Convert response to dictionary
        # Extract the 'data' list of words from the dictionary
        global word_list
        word_list = data.get("data", [])

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the word list: {e}")
def get_valid_word(word_list):
    word = random.choice(word_list)
    while '-' in word or '' in word:
        word = random.choice(word_list)

    return word

def hangman():
    word = get_valid_word(word_list)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives,'Lives left and You have used these  letters: ', ' '.join(used_letters))

        # what current word is (i.e W - R D)
        words_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(words_list))

        user_letter = input('Guess a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('Letters is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0  or when lives == 0
    if lives == 0:
        print('You died, Sorry. The word was', word)
    else:
        print('You guesssed the word', word, '!!')
# Fetch the words once

fetch_words() 
hangman()


