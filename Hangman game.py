import random
words = ["python", "java", "hangman", "programming", "computer",]
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []
print("Welcome to Hangman Game!")
while attempts > 0 and "_" in guessed_word:
    print("Word:", " ".join(guessed_word))
    print("Attempts left:", attempts)
    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1
if "_" not in guessed_word:
    print("You won! The word was:", word)
else:
    print("You lost! The word was:", word)
