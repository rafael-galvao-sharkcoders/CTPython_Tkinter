import tkinter as tk
import os

root = tk.Tk()
root.title("Tic Tac Tac")

current_player = "X"
game_board = [" " for _ in range(9)]
player1_name = ""
player2_name = ""


ranking_file = "ranking.txt"

def check_winner():
    # Check rows
    for i in range(0, 9, 3):
        if game_board[i] == game_board[i+1] == game_board[i+2] != " ":
            return True
    # Check columns
    for i in range(3):
        if game_board[i] == game_board[i+3] == game_board[i+6] != " ":
            return True
    # Check diagonals
    if game_board[0] == game_board[4] == game_board[8] != " ":
        return True
    if game_board[2] == game_board[4] == game_board[6] != " ":
        return True
    return False

def update_ranking(winner_name):
    if os.path.exists(ranking_file):
        with open(ranking_file, 'r') as file:
            lines = file.readlines()
            ranking  = {line.split(':') [0]: int(line.split(':')[1]) for line in lines}
        
        if winner_name in ranking:
            ranking[winner_name] += 1 
        
        else:
            ranking[winner_name] = 1
        
        with open(ranking_file, 'w') as file:
            for name, wins in ranking.items():
                file.write(f"{name}:{wins}\n")
    
    else:
        with open(ranking_file, 'w') as file:
            file.write(f"{winner_name}\n")

def on_click(square_index): 
    if game_board[square_index] == " ":
        global current_player
        game_board[square_index] = current_player
        button = buttons[square_index]
        button.config(text=current_player)
        if check_winner():
            winner_label.config(text=f"Player {current_player} wins!")
            update_ranking(player1_name if current_player == "X" else player2_name)
            for i in buttons:
                i.config(state="disabled")
        else:
            current_player = "O" if current_player == "X" else "X"
            player_label.config(text=f"Current Player: {current_player} ({player1_name if current_player == 'X' else player2_name})")

def start_game():
    global player1_name, player2_name
    player1_name = entry1.get()
    player2_name = entry2.get()
    player_label.config(text=f"Current Player: X ({player1_name})")
    start_button.config(state="disabled")
    for button in buttons:
        button.config(state="active")
    entry1.config(state="disabled")
    entry2.config(state="disabled")

buttons = []
for i in range(9):
    row = i // 3
    col = i % 3
    button = tk.Button(root, text=" ", width=10, height=3, command=lambda i=i: on_click(i), state="disabled")
    button.grid(row=row, column=col)
    buttons.append(button)

player_label = tk.Label(root, text=f"Current Player: {current_player}")
player_label.grid(row=3, column=0, columnspan=3)

winner_label = tk.Label(root, text="")
winner_label.grid(row=4, column=0, columnspan=3)

player1_label = tk.Label(root, text="Enter Player 1 Name:")
player1_label.grid(row=5, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=5, column=1)

player2_label = tk.Label(root, text="Enter Player 2 Name:")
player2_label.grid(row=6, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=6, column=1)

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.grid(row=7, column=0, columnspan=2)

root.mainloop()

