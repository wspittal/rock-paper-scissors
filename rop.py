import random

rps = [
    "rock",
    "paper",
    "scissors"
]

win  = 0
lose = 0
tie  = 0

while True:
    computer = (random.choice(rps))
    player = ""
  
    while rps.count(player) != 1 and player != "gun":
        player = input("Rock, Paper, Scissors, or Gun?\n").lower()
    
    if player == computer:
        print("I play " + player + "! We tie!")
        tie += 1
    
    elif player == "rock":
        if computer == "paper":
            print("I play paper! You lose!")
            lose += 1
        else:
            print("I play scissors! You win!")
            win += 1
    
    elif player == "paper":
        if computer == "scissors":
            print("I play scissors! You lose!")
            lose += 1
        else:
            print("I play rock! You win!")
            win += 1
    
    elif player == "scissors":
        if computer == "rock":
            print("I play rock! You lose...")
            lose += 1
        else:
            print("I play paper! You win!")
            win += 1
    
    elif player == "gun":
        print("You don't deserve to play rock paper scissors")
        break
    
    print("\nWin - " + str(win) + "\nLose - " + str(lose) + "\nTie - " + str(tie) + "\n")
    
    c = input("Type R to restart or anything else to end. ").lower()
    
    if c != "r":
        print("Bye Then!")
        break
