import random

# --- Task 1: play_rock_paper_scissors ---
def play_rock_paper_scissors(player_choice, comp_choice):
    """
    Play a round of the Rock-Paper-Scissors game.

    Parameters:
        player_choice (str): The choice of Player 1. Should be one of 'rock', 'paper', or 'scissors'.
        comp_choice (str): The choice of Computer. Should be one of 'rock', 'paper', or 'scissors'.

    Returns:
        str: The result of the round. It can be one of the following:
             - "Tie" if both players have the same choice.
             - "Player 1 wins" if Player 1's choice wins the round.
             - "Comp wins" if Computer's choice wins the round.

    Example:
        >>> play_rock_paper_scissors('rock', 'paper')
        'Comp wins'
        >>> play_rock_paper_scissors('scissors', 'scissors')
        'Tie'
    """
    valid_choices = {'rock', 'paper', 'scissors'}

    # Normalize inputs just in case
    player_choice = player_choice.lower()
    comp_choice = comp_choice.lower()

    # Check if it's a tie
    if player_choice == comp_choice:
        result = "Tie"

    # Determine the winner based on the rules
    elif (player_choice == 'rock' and comp_choice == 'scissors') or \
         (player_choice == 'paper' and comp_choice == 'rock') or \
         (player_choice == 'scissors' and comp_choice == 'paper'):
        result = "Player 1 wins"
    else:
        result = "Comp wins"

    return result


# --- Task 2: computer_makes_choice ---
def computer_makes_choice():
    """
    Generates the choice of the computer in the Rock-Paper-Scissors game.

    Parameters:
        none.

    Returns:
        str: The choice of the computer. Should be one of 'rock', 'paper', or 'scissors'.

    Example:
        >>> computer_makes_choice()
        'rock'
        >>> computer_makes_choice()
        'scissors'
    """
    valid_choices = {'rock', 'paper', 'scissors'}

    # Generate computer's choice randomly
    # Converting the set to a list because random.choice needs an indexable sequence
    result = random.choice(list(valid_choices))

    return result


# --- Task 3: play_multiple_rounds ---
def play_multiple_rounds(num_rounds):
    """
    Play multiple rounds of the Rock-Paper-Scissors game against the computer.

    Parameters:
        num_rounds (int): The number of rounds to play.

    Returns:
        None

    Example:
        >>> play_multiple_rounds(3)
        Enter your choice (rock/paper/scissors): rock
        Round 1: You chose rock. Computer chose paper. Comp wins

        Enter your choice (rock/paper/scissors): paper
        Round 2: You chose paper. Computer chose paper. Tie

        Enter your choice (rock/paper/scissors): scissors
        Round 3: You chose scissors. Computer chose rock. Comp wins
    """
    valid_choices = {'rock', 'paper', 'scissors'}

    # Implementation of the dialog with the player
    for round_num in range(1, num_rounds + 1):
        # Get user input
        player_choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()
        
        # Simple input validation loop to ensure game flow stays correct
        while player_choice not in valid_choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            player_choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()

        # Get computer choice
        comp_choice = computer_makes_choice()
        
        # Determine round winner
        round_result = play_rock_paper_scissors(player_choice, comp_choice)
        
        # Display the result formatted exactly like the docstring example
        print(f"Round {round_num}: You chose {player_choice}. Computer chose {comp_choice}. {round_result}\n")

    return None


# Example usage:
if __name__ == "__main__":
    num_rounds = int(input("Enter the number of rounds to play: "))
    play_multiple_rounds(num_rounds)
        


#import streamlit as st
#import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
