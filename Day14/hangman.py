import random
import time

name = input("Enter your name: ")
print("Hello " +name, "time to play hangman!")

time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

words = ["python", "secret", "pyandrei"]
word = random.choice(words)

gueses = ""
turns = 10

while turns>0:
    failed = 0
    for char in word:
        if char in gueses:
            print(char,end=""),
        else:
            print("_",end="")
            failed+=1
        pass
    if failed == 0:
        print("\nYou win!")
        break
    guess = input("Guess a character:")
    gueses += guess
    turns -= 1
    print("Wrong!")
    print("You have", +turns, "more guesses")
    if turns == 0:
        print("You lose")
    pass