import random
options = ("rock","paper","scissors")
print("Rules")
print("Rock beats scissors")
print("Paper beats rock")
print("scissor beats paper")
play = True
while play:
    player = None
    computer_choice = random.choice(options)
    while player not in options:
        player = input("Enter a choice(rock, paper, scissors):")
        if player not in options:
            print("invalid option!")
        else:    
            print(f"Player:{player}")
            print(f"computer:{computer_choice}")
            if player == computer_choice:
                print("The game is draw!")
            elif player == "rock" and computer_choice == "paper" or player == "scissors" and computer_choice == "rock" or player == "paper" and computer_choice == "scissors":
                print("computer wins!")
            elif player == "rock" and computer_choice == "scissors" or player == "paper" and computer_choice == "rock" or player == "scissors" and computer_choice == "paper":    
                print("You wins!")

            play_again = input("play again? (y/n):").lower()
            if not play_again == "y":
                play = False   
print("Thanks for playing.........")
