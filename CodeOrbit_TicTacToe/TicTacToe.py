# Task 2: Tic-Tac-Toe with Simple AI
# Author: CodeOrbit Tech Intern
# Description: A command-line Tic-Tac-Toe game where the user plays against 
# a rule-based AI opponent that tries to win or block player moves.

import random

def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board, player):
    # All possible winning combinations
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == player and board[condition[1]] == player and board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    return all(spot != " " for spot in board)

def ai_move(board):
    # Step 1: Check if AI can win in the next move
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner(board, "O"):
                return i
            board[i] = " "
            
    # Step 2: Check if Player can win in the next move, and block them
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner(board, "X"):
                board[i] = "O"
                return i
            board[i] = " "
            
    # Step 3: Otherwise, pick a random available spot
    empty_spots = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(empty_spots) if empty_spots else None

def play_tic_tac_toe():
    board = [" " for _ in range(9)]
    print("Welcome to Tic-Tac-Toe! You are 'X' and the AI is 'O'.")
    print("Positions correspond to numbers 1 through 9:")
    print_board([str(i + 1) for i in range(9)])
    
    current_player = "X" # User goes first

    while True:
        if current_player == "X":
            move = input("Your turn! Choose a position (1-9): ")
            if not move.isdigit() or not (1 <= int(move) <= 9):
                print("Invalid input! Please enter a number between 1 and 9.")
                continue
            index = int(move) - 1
            if board[index] != " ":
                print("That spot is already taken! Choose another.")
                continue
            board[index] = "X"
        else:
            print("AI is making a move...")
            index = ai_move(board)
            board[index] = "O"
            
        print_board(board)
        
        # Check win condition
        if check_winner(board, current_player):
            if current_player == "X":
                print("Congratulations! You won!")
            else:
                print("AI wins! Better luck next time.")
            break
            
        # Check draw condition
        if is_board_full(board):
            print("It's a draw!")
            break
            
        # Switch turns
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_tic_tac_toe()