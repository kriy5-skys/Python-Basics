import random
data = ["rock","paper","scissors"]

while True:
    user_guess = input("Rock, Paper or Scissors?: ").lower()
    comp_guess = random.choice(data)
    if ((user_guess == "rock" and comp_guess == "scissors") or (user_guess == "scissors" and comp_guess == "paper") or 
    (user_guess == "paper" and comp_guess == "rock")):
        print("Computer guess is: ", comp_guess)
        print("User has won!!")
    elif ((comp_guess == "rock" and user_guess == "scissors") or (comp_guess == "scissors" and user_guess == "paper") or 
    (comp_guess == "paper" and user_guess == "rock")):
        print("Computer guess is: ", comp_guess)
        print("Computer has won!!")
    elif (comp_guess == user_guess):
        print("Computer guess is: ", comp_guess)
        print("It's a tie!!")
    else:
        print("WRONG INPUT!")
    break