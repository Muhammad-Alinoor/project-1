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
    elif player == "rock":
        if computer == "scissor":
            return "Rock smashed scissor! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissor cuts paper! You lose."
    else:
        if computer == "paper":
            return "Scissor cuts paper! You win."
        else:
            return "Rock smashed scissor! You lose."
choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)