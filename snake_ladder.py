import random
import tkinter as tk
from tkinter import messagebox

# Snake and Ladder board mapping
board = {
    2: 23, 8: 12, 18: 45, 26: 47, 36: 55, 44: 68, 52: 72, 60: 79, 70: 89,
    95: 75, 99: 7, 92: 34, 80: 41, 64: 24, 50: 5
}

class SnakeLadderGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake and Ladder")
        self.root.geometry("400x400")

        self.player_pos = 1
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to Snake and Ladder!", font=("Arial", 14))
        self.label.pack(pady=10)

        self.dice_label = tk.Label(self.root, text="Roll the dice", font=("Arial", 12))
        self.dice_label.pack(pady=10)

        self.roll_button = tk.Button(self.root, text="Roll Dice 🎲", font=("Arial", 14), command=self.roll_dice)
        self.roll_button.pack(pady=10)

        self.position_label = tk.Label(self.root, text=f"Current Position: {self.player_pos}", font=("Arial", 12))
        self.position_label.pack(pady=10)

    def roll_dice(self):
        roll = random.randint(1, 6)
        self.dice_label.config(text=f"Dice Roll: {roll}")

        new_pos = self.player_pos + roll

        if new_pos in board:
            new_pos = board[new_pos]

        if new_pos > 100:
            new_pos = self.player_pos  # Stay in place if exceeding 100

        self.player_pos = new_pos
        self.position_label.config(text=f"Current Position: {self.player_pos}")

        if self.player_pos == 100:
            messagebox.showinfo("Congratulations!", "You won the game!")
            self.reset_game()

    def reset_game(self):
        self.player_pos = 1
        self.position_label.config(text=f"Current Position: {self.player_pos}")
        self.dice_label.config(text="Roll the dice")

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeLadderGame(root)
    root.mainloop()
