import random
#choice 
def get_choices():
    player_choice = input()
    options = ["rock","paper","scissor"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices
#response = get_choices()
#print(response)

def check_win(player,computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a Tie!"
check_win("rock","paper")