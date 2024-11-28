from random import randint
import keyboard
import time

ans = "Y"

while ans == "Y":
    x = randint(1, 6)

    if x == 1:
        print("[-----]")
        print("[-----]")
        print("[--o--]")
        print("[-----]")
        print("[-----]")
    elif x == 2:
        print("[-----]")
        print("[-o---]")
        print("[-----]")
        print("[---o-]")
        print("[-----]")
    elif x == 3:
        print("[-----]")
        print("[-----]")
        print("[-ooo-]")
        print("[-----]")
        print("[-----]")
    elif x == 4:
        print("[-----]")
        print("[-o-o-]")
        print("[-----]")
        print("[-o-o-]")
        print("[-----]")
    elif x == 5:
        print("[-----]")
        print("[-o-o-]")
        print("[--o--]")
        print("[-o-o-]")
        print("[-----]")
    elif x == 6:
        print("[-----]")
        print("[-o-o-]")
        print("[-o-o-]")
        print("[-o-o-]")
        print("[-----]")

    print("Press Y to roll again or N to exit\n")

    while True:
        if keyboard.is_pressed('y'):
            ans = "Y"
            break
        elif keyboard.is_pressed('n'):
            ans = "N"
            break

    time.sleep(0.1)
