import random
from socket import if_indextoname

# Load wrods from a file
def load_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().splitlines()
            if not words:
                print("The Word list is Empty. Add some words to the file.")
            return words
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return []
    
# Hangman Game Logic
def play_hangman(words):
    word = random.choice(words).lower()
    guessed_words = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    print("\nWelcome to Hangman Game!")
    print("Guess the word by entering one letter at a time.")

    while attempts > 0 and "_" in guessed_words:
        print("\nWord: ", " ".join(guessed_words))
        print("Attempts Left: ", attempts)
        print("Guessed Letters: ", " ".join(guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input. Please enter a single Alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You have already guessed this letter.")
        elif guess in word:
            print("Good Guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_words[i] = guess
            
            guessed_letters.add(guess)
        else:
            print("Incorrect Guess!")
            attempts -= 1
            guessed_letters.add(guess)

    if "_" not in guessed_words:
        print("\n✨Congratulations! You have guessed the word correctly.✨")
        print("The word is: ", word)
    else:
        print("\n💀You lost the game. The word was: ", word)

def main():
    print("Hangman Game")
    words = load_words("D:\\101 Python Course 2025\\Intermediate\\Projects\\Hangman Game\\words.txt")
    if not words:
        return

    while True:
        play_hangman(words)
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThank you for playing Hangman Game.")
            break
    
if __name__ == "__main__":
    main()
