print("rock paper scissors")
input("press enter to start")
print ("Game starting . . .  type rock, paper, or scissors to play")
import random
choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
def play_game():
    player_score = 0
    computer_score = 0
    while player_score < 3 and computer_score < 3:
        computer = random.choice(choices)
        player = input("rock, paper, or scissors?: ").strip().lower()
        if  player=="rock" and computer=="rock":
            print("Tie: both chose rock")
        elif player=="rock" and computer=="paper":
            computer_score = computer_score + 1
        elif player=="rock" and computer=="scissors":
            player_score = player_score + 1
        elif player=="paper" and computer=="rock":
            player_score = player_score + 1
        elif player=="paper" and computer=="paper":
            print("Tie: both chose paper")
        elif player=="paper" and computer=="scissors":
            computer_score = computer_score + 1
        elif player=="scissors" and computer=="rock":
            computer_score = computer_score + 1
        elif player=="scissors" and computer=="paper":
            player_score = player_score + 1
        elif player=="scissors" and computer=="scissors":
            print("Tie: both chose scissors")
        else:
            print("invalid choice")
            continue
        print(f"Computer chose: {computer}. Score - You: {player_score} Computer: {computer_score}")
    if player_score == 3:    
        print("you win")
        print("GAME OVER")
    else:   
        print("you lose")
        print("GAME OVER")
    answer = input("Do you want to play again? (y/n): ").strip().lower()
    if answer == "y" or answer == "yes":
        play_game()
    elif answer == "n" or answer == "no":
        print("Thanks for playing!")
    else:
        print("invalid input")
play_game()