import tkinter as tk
 
root = tk.Tk()
root.title("Tic Tac Tac")
 
current_player = "X"
game_board = [" " for _ in range(9)]
 
def check_winner():
    #linhas
    for i in range(0, 9, 3):
        if game_board[i] == game_board[i+1] == game_board[i+2] != " ":
            return True
    #colunas
    for i in range(3):
        if game_board[i] == game_board[i+3] == game_board[i+6] != " ":
            return True
    #diagonais
    if game_board[0] == game_board[4] == game_board[8] != " ":
            return True
    if game_board[2] == game_board[4] == game_board[6] != " ":
            return True
    return False
 
 
def on_click(square_index):
    if game_board[square_index] == " ":
        global current_player
        game_board[square_index] = current_player
        button = buttons[square_index]
        button.config(text=current_player)
        if check_winner():
            winner_label.config(text=f"Player {current_player} wins!")
            for i in buttons:
                i.config(state="disabled")
        else:
            current_player = "0" if current_player == "X" else "X"
            player_label.config(text=f"Current Player: {current_player}")
 
 
buttons = []
for i in range(9):
    row = i // 3
    col = i % 3
    button = tk.Button(root, text=" ", width=10, height=3, command=lambda i=i: on_click(i))
    button.grid(row=row, column=col)
    buttons.append(button)
    
player_label = tk.Label(root, text=f"Current Player: {current_player}")
player_label.grid(row=3, column=0, columnspan=3)
 
winner_label = tk.Label(root, text="")
winner_label.grid(row=4, column=0, columnspan=3)
 
root.mainloop()
