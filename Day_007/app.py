import random
import hangman_words
import hangman_art

lives = 6

print(hangman_art.logo)
print("WELCOME TO THE HANGMAN GAME!!!")

chosen_word = random.choice(hangman_words.words)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

gameover = False
correct_letters = []
chosen_letters = []

while not gameover:
    print(f"************************{lives}/6 LIVES LEFT************************")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter!")
        continue

    if guess in chosen_letters:
        print(f"You've already guessed {guess}")
        continue

    chosen_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            gameover = True
            print(f"************************IT WAS {chosen_word}! YOU LOSE************************")

    if "_" not in display:
        gameover = True
        print("************************YOU WIN!************************")

    print(hangman_art.stages_hangman[lives])
