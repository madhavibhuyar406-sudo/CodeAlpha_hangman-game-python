import random

def hangman():
    # List of 5 predefined words as per the simplified scope
    words = ["python", "code", "alpha", "game", "learn"]
    
    # Select a random word from the list
    word_to_guess = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6  # Limit incorrect guesses to 6
    
    print("Welcome to Hangman Game!")
    print(f"You need to guess the word. You have a maximum of {max_incorrect} incorrect guesses.")
    
    while incorrect_guesses < max_incorrect:
        # Display the current state of the word (unguessed letters shown as '_')
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
                
        print("\nWord: ", display_word.strip())
        
        # Check if all letters have been guessed
        if "_" not in display_word:
            print("Congratulations! You guessed the word correctly!")
            break
            
        # Get input from the user
        guess = input("Guess a letter: ").lower()
        
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid alphabetical character.")
            continue
            
        if guess in guessed_letters:
            print("You have already guessed that letter. Try a different one.")
            continue
            
        guessed_letters.append(guess)
        
        # Check if the guessed letter is in the word
        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            remaining = max_incorrect - incorrect_guesses
            print(f"Wrong! '{guess}' is not in the word. Remaining attempts: {remaining}")
            
    else:
        print("\nGame Over!")
        print(f"The correct word was: {word_to_guess}")

# Run the game
if __name__ == "__main__":
    hangman()
