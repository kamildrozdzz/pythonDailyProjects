import random
from functions import(
    choiceName,
    whoWins
)

print("Winning rules of the game Rock Paper Scissors are:\n"
      +"Rock vs Paper -> Paper wins\n"
      +"Rock vs Scissors -> Rock wins\n"
      +"Paper vs Scissors -> Scissors wins")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    
    #take input from user...
    choice = int(input("Enter your choice: "))

    while choice<1 or choice>3:
        choice = int(input("Enter a vaild choice, please: "))
    pass

    choice_name = choiceName(choice)
    print("Now is computer turn")

    comp_choice = random.randint(1,3)

    while comp_choice == choice:
        comp_choice = random.randint(1,3)


    comp_choice_name = choiceName(comp_choice)
    print(choice_name,"VS",comp_choice_name)

    result = whoWins(choice, comp_choice)
    # Printing whether the user or computer wins, or if it's a draw
    if result == "DRAW":
        print("<== It's a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    ans = input("Do you want to play again? (Y/N): ").lower
    if ans == 'n':
        break
print("Thanks for playing!")