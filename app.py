import random
#Ask the user to choose between rock, paper and scissors
player_choice = input('Enter a choice between R, P, S \n')

# Make the computer choose. This allows a random item to be selected from the list.
possible_actions = ['R', 'P', 'S']
computer_choice = random.choice(possible_actions)

# Print the computer's choice and the user's player_choice
print(f'PlAYER {player_choice}: CPU {computer_choice}. \n')

# Decide the winner using if/else statements

if player_choice == computer_choice:
    print(f'Both players selected {player_choice}. It\'s a tie')
elif player_choice == "R":
    if computer_choice == "S":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif player_choice == "P":
    if computer_choice == "R":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif player_choice == "S":
    if computer_choice == "P":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
else:
    print(input('Wrong choice. Please pick between R, P and S and ensure your option is in uppercase \n'))
        