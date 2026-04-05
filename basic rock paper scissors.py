import random

data = ["Rock", "Paper", "Scissors"]

def result():
    return random.choice(data)
while True:
    user = input("Rock, Paper or Scissors (or quit to stop): ").capitalize()

    if user == "Quit":
        print('thanks for playing')
        break

    if user not in data:
        print('Son')
        continue

    computer = result()
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("tie")
    elif user == "Rock":
        if computer == "Scissors":
            print("you win")
        else:
            print('You lose')
    if user == "Paper":
        if computer == "Rock":
            print("you win")
        else:
            print("you lose")
    if user == "Scissors":
        if computer == "Paper":
            print("you win")
        else:
            print("you lose")
        

    

    
        

