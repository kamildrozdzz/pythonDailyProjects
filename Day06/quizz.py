questions = (
    "What countries are in Europe?: ",
    "What is the strongest phone in the world?: ",
    "How many letters are in the Chinese alphabet?: ",
    "What is the hardest language to learn?: ",
    "How many bhp has Koenigsegg Jesko Absolut?: "
)

options = (
    ("A.42", "B.46", "C.44", "D.39"),
    ("A.Nokia 3310", "B.Samsung Galaxy Note 7", "C.Sonim XP3300 Force", "D.iPhone SE2"),
    ("A.36", "B.45", "C.5,000", "D.20,000"),
    ("A.Hungary", "B.Mandarin", "C.Chinese", "D.Japanese"),
    ("A.1000", "B.950", "C.1320", "D.1280")
)

answers = ("C", "C", "A", "B", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("WHO WANTS TO BE A BILLIONAIRE")
    print("")
    print("-------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
    
    question_num += 1

print(f"Your final score is {score}/{len(questions)}")
