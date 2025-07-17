import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe Ultimate")
        self.master.geometry("600x700")
        self.master.resizable(False, False)

        # OPTIONAL: Set your own icon if you have one:
        # self.master.iconbitmap('tictactoe.ico')

        self.player1_marker = tk.StringVar(value="X")
        self.player2_marker = "O"
        self.turn = "X"
        self.board = ["*"] * 9
        self.buttons = []

        self.build_marker_selection()

    def build_marker_selection(self):
        self.clear_window()

        tk.Label(self.master, text="Choose Your Marker", font=("Arial", 24)).pack(pady=40)
        frame = tk.Frame(self.master)
        frame.pack()

        tk.Radiobutton(frame, text="X", variable=self.player1_marker, value="X",
                       font=("Arial", 20)).grid(row=0, column=0, padx=20)
        tk.Radiobutton(frame, text="O", variable=self.player1_marker, value="O",
                       font=("Arial", 20)).grid(row=0, column=1, padx=20)

        tk.Button(self.master, text="Start Game", font=("Arial", 20),
                  command=self.start_game).pack(pady=40)

    def start_game(self):
        self.player2_marker = "O" if self.player1_marker.get() == "X" else "X"
        self.turn = "X"
        self.board = ["*"] * 9
        self.build_board()

    def build_board(self):
        self.clear_window()

        self.status_label = tk.Label(self.master, text=f"{self.turn}'s Turn",
                                     font=("Arial", 20))
        self.status_label.pack(pady=20)

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.buttons = []
        for i in range(9):
            b = tk.Button(self.frame, text=" ", width=10, height=5,
                          font=("Arial", 24, "bold"),
                          command=lambda i=i: self.make_move(i),
                          bg="#f0f0f0")
            b.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(b)

    def make_move(self, i):
        if self.board[i] == "*":
            marker = self.get_current_marker()
            self.board[i] = marker
            self.buttons[i].config(text=marker, disabledforeground="#000000")
            self.buttons[i].config(state="disabled", bg="#d0f0c0" if marker == "X" else "#f0d0d0")

            if self.check_winner(marker):
                self.end_game(f"{marker} Wins!")
            elif "*" not in self.board:
                self.end_game("It's a Tie!")
            else:
                self.turn = "O" if self.turn == "X" else "X"
                self.status_label.config(text=f"{self.turn}'s Turn")

    def get_current_marker(self):
        if self.turn == "X":
            return "X" if self.player1_marker.get() == "X" else "O"
        else:
            return "O" if self.player1_marker.get() == "X" else "X"

    def check_winner(self, marker):
        combos = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        return any(all(self.board[i]==marker for i in combo) for combo in combos)

    def end_game(self, result):
        messagebox.showinfo("Game Over", result)
        self.start_game()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
