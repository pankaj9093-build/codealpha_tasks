import random
word_list = ["apple", "banana", "grape", "orange", "peach","papaya","guava","grapes"]
chosen_word = random.choice(word_list)
lives = 6
display = ['_' for _ in chosen_word]
game_over = False

print("Welcome to Hangman!")
print("The word has", len(chosen_word), "letters.")

while not game_over:
    print("\nCurrent word: " + " ".join(display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
        print("Good guess!")
    else:
        lives -= 1
        print(f" Wrong guess. Lives remaining: {lives}")

    if "_" not in display:
        print("\n You win! The word was:", chosen_word)
        game_over = True

    if lives == 0:
        print("\n You lose! The word was:", chosen_word)
        game_over = True
