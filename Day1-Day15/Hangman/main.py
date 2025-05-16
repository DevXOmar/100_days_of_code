import random
import hangman_words ## importing the file hangman.py
import hangman_art
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
all_entry = []
while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"Lives left: {lives}")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    display = ""
    if guess in all_entry:
        print(f"You already chose the letter {guess}")
    elif guess not in chosen_word:
        lives -= 1

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            all_entry.append(guess)
        elif letter in correct_letters:
            display += letter
            all_entry.append(guess)
        else:
            display += "_"
            all_entry.append(guess)

    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.


    if lives == 0:
        game_over = True
        print(f"***********************YOU LOSE**********************")

        # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(hangman_art.stages[lives])
