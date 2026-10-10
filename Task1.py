import random

# 1. List of 5 predefined words
words = ["python", "internship", "program", "keyboard", "developer"]

# 2. Pick a random word and set up the game state
secret_word = random.choice(words)
guessed_letters = []          # all letters the player has tried
wrong_guesses = 0
max_wrong = 6

print("=== HANGMAN ===")
print("Guess the word one letter at a time. You have 6 wrong guesses.\n")

# 3. Main game loop
while wrong_guesses < max_wrong:
    # Build the display string, e.g. "p _ t h _ n"
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("Word:", display)
    print("Wrong guesses left:", max_wrong - wrong_guesses)
    print("Guessed so far:", ", ".join(guessed_letters))

    # Check for a win (no underscores left)
    if "_" not in display:
        print("\nCongratulations! You guessed the word:", secret_word)
        break

    # Get and validate the player's guess
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check if the guess is right or wrong
    if guess in secret_word:
        print("Good guess!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess!\n")

# 4. If the loop ended because guesses ran out, the player lost
else:
    print("Game over! The word was:", secret_word)