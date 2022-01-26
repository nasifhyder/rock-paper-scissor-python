import random

keep_going = True
computer_score = 0
score = 0
draw = "Round Tied"
loss = "Round lost"
win = "Round Won"
rock = "rock"
paper = "paper"
scissor = "scissor"
option = [rock, paper, scissor]

while keep_going:
    choice = input("your choice:").lower()
    computers_choice = random.choice(option)
    print(computers_choice)

    if computers_choice == choice:
        print(draw)
        print(f"You:{score} Computer:{computer_score}")
    elif computers_choice != choice:
        if computers_choice == rock and choice == paper or computers_choice == paper and choice == scissor or \
                computers_choice == scissor and choice == rock:
            score += 1
            print(win)
            print(f"You:{score} Computer:{computer_score}")

        elif choice == rock and computers_choice == paper or choice == paper and computers_choice == scissor or \
                choice == scissor and computers_choice == rock:
            computer_score += 1
            print(loss)
            print(f"You:{score} Computer:{computer_score}")

    elif choice == "stop":
        keep_going = False
