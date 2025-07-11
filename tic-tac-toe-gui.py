# 🎮 Aesthetic Tic Tac Toe Game by Prince Pathak using Tkinter

import tkinter as tk
from tkinter import messagebox

# 🌈 Game colors and styles
BG_COLOR = "#2e2e2e"
BTN_COLOR = "#4caf50"
FONT = ("Segoe UI", 24)
PLAYER_X = "❌"
PLAYER_O = "⭕"

# 🧠 Initialize variables
current_player = PLAYER_X
board = [["" for _ in range(3)] for _ in range(3)]

# 🎯 Handle a button click
def handle_click(row, col):
    global current_player

    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")

        if check_winner(current_player):
            messagebox.showinfo("🏆 Game Over", f"{current_player} wins! 🎉")
            reset_game()
        elif check_draw():
            messagebox.showinfo("🤝 Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X
            status_label.config(text=f"{current_player}'s Turn")

# ✅ Check for a winner
def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# ⛔ Check for a draw
def check_draw():
    return all(board[i][j] != "" for i in range(3) for j in range(3))

# 🔄 Reset game
def reset_game():
    global current_player, board
    current_player = PLAYER_X
    board = [["" for _ in range(3)] for _ in range(3)]
    status_label.config(text=f"{current_player}'s Turn")
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")

# 🎨 GUI Setup
root = tk.Tk()
root.title("Tic Tac Toe - Prince Edition 🎮")
root.config(bg=BG_COLOR)
root.geometry("400x500")

# 📢 Status label
status_label = tk.Label(root, text=f"{current_player}'s Turn", font=("Segoe UI", 20), bg=BG_COLOR, fg="white")
status_label.pack(pady=20)

# 🔘 Button grid
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack()

buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        btn = tk.Button(frame, text="", font=FONT, width=5, height=2,
                        bg=BTN_COLOR, fg="white",
                        command=lambda r=i, c=j: handle_click(r, c))
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = btn

# 🔁 Reset Button
reset_btn = tk.Button(root, text="🔄 Reset Game", font=("Segoe UI", 14),
                      command=reset_game, bg="#f44336", fg="white")
reset_btn.pack(pady=20)

# 🚀 Run the app
root.mainloop()
# 🏁 End of the game
# 🎉 Enjoy playing Tic Tac Toe! 🕹️