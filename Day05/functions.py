def choiceName(number):
    if number == 1:
            choice_name = "Rock"
    elif number == 2:
            choice_name = "Paper"
    else:
            choice_name = "Scissors"
    print("Your choice is", choice_name)
    return choice_name
    pass

def whoWins(choice, comp_choice):
    if (choice == 1 and comp_choice == 2):
        print("Paper wins =>", end="")
        return "paperR"
    elif (choice == 2 and comp_choice == 1):
        print("Paper wins =>", end="")
        return "Paper"

    if (choice == 1 and comp_choice == 3):
        print("Rock wins =>\n", end="")
        return "Rock"
    elif (choice == 3 and comp_choice == 1):
        print("Rock wins =>\n", end="")
        return "rock"

    if (choice == 2 and comp_choice == 3):
        print("Scissors wins =>", end="")
        return "scissor"
    elif (choice == 3 and comp_choice == 2):
        print("Scissors wins =>", end="")
        return "Rock"
    pass