import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0


    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        # Define the RPS Enum inside the function or outside if preferred
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # Get the player's choice
        playerchoice = input(f"\n{name}, please enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")
        
        # Validate the player's input
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        # Convert player's choice to an integer
        player = int(playerchoice)
        
        # Randomly choose for the computer (use integers directly)
        computerchoice = random.choice([1, 2, 3])

        computer = int(computerchoice)

        # Display both player and computer choices
        print(f"\n{name} you chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")
    

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            # Determine the winner
            if player == 1 and computer == 3: 
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == 2 and computer == 1: 
                player_wins += 1
                return f"🎉{name}, you win!"
            elif player == 3 and computer == 2: 
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins! \nSorry, {name}..😭"
        
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print(f"\nPlay again?, {name}?")

        # Ask the user if they want to play again
        while True:
            playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n").lower()
            
            # Check if the input is valid (Y or Q)
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break 
        # If player wants to play again, restart the game
        if playagain.lower() == "y":
            return play_rps()
        else:
            # Exit the game
            print("\n🎉 🎉 🎉 🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Bye {name}! 👋")

    return play_rps
    # Start the game



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description = "Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar = "name",
        required=True, help = "The name of the person playing the game."
    )
    
    args = parser.parse_args()


    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()

