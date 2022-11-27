import random
print("************************************* RPS,  ROCK,PAPER, SCISSORS****************************************")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computers_choice = random.randint(0,2)
print(f"Computer chose {computers_choice}")

if user_choice == 0 and computers_choice == 2:
    print("You win!")
elif computers_choice > user_choice:
    print("You lose")
elif computers_choice == user_choice:
    print("Its a draw")
else:
    print("You entered an invalid number, you lose!")