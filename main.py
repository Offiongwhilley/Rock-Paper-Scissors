import random

play = True
while play == True:
    game = input("Do you wish to play? y/n \n").lower()
    if (game == 'y'):
        print("R - Rock\nP - Paper\nS - Scissors")
        player = input("Choose between R, S, P\n")
        
        # play = "true"
        select = ["Rock", "Paper", "Scissors"]
        choices = ['R', 'P', 'S']
        computer = random.choice(choices)
        
        if computer == player:
            print(f"it's a tie!!! Play again.")
            play = True
            
        elif computer == 'R'and player == 'S':
            print(f"computer ({select[0]}) : Player ({select[2]})")
            print(f"The computer wins this round with {computer}: Rock which smashes {player}: Scissors")
            play = False
            
        elif computer == 'P' and player == 'R':
            print(f"computer ({select[1]}) : Player ({select[0]})")
            print(f"The computer wins this round with {computer}: Paper which covers {player}: Rock")
            play = False
            
        elif computer == 'S' and player == 'P':
            print(f"computer ({select[2]}) : Player ({select[1]})")
            print(f"The computer wins this round with {computer}: Scissors which can cut through {player}: paper")
            play = False
            
        elif computer == 'R' and player == 'P':
            print(f"computer ({select[0]}) : Player ({select[1]})")
            print(f"Paper covers rock! You win with {player}: Paper")
            play = False
            
        elif computer == 'P' and player == 'S':
            print(f"CPU ({select[1]}) : Player ({select[2]})")
            print("Scissors cuts paper! You win with {player}: Scissors")
            play = False
            
        elif computer == 'S' and player == 'R':
            print(f"CPU ({select[2]}) : Player ({select[0]})")
            print(f"Rock smashes Scissors! You win!!!")
            play = False
            
        else:
            print("Invalid option. Try again and make sure you selection is in upper case.")
            play = True
    
    elif (game == 'n'):
        print("Have a nice day!!!\n")
        break

    else:
        print("Invalid selection.")
