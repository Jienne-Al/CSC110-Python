word = "broom"
life = 4
guessed = ["_"] * len(word)

print("Welcome to Hangman Lite!")
print(" ".join(guessed))

while life > 0:
    letter = input("Give me a letter: ")
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print("Correct!", " ".join(guessed))

        if "".join(guessed) == word:
            print("Congratulations, you guessed the word!")
            break
    else:
        life -= 1
        print(f"Wrong! {life} attempts left.")

    if life == 0:
        print(f"Game over. The word was '{word}'.")
