from random import(
    randint
)

x = randint(1,10)
guess = None

while guess != x:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == x:
        print("Congratulations, you win!")
        break
    else:
        print("Try again...")
    pass