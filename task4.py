import random
import tkinter as tk
from tkinter import messagebox

def rock_paper_scissors(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        return f"Both players selected {player_choice}. It's a tie!", computer_choice
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return f"You win! {player_choice} beats {computer_choice}", computer_choice
    else:
        return f"You lose! {computer_choice} beats {player_choice}", computer_choice

def player_choice(choice):
    global user_score, computer_score
    result, computer_choice = rock_paper_scissors(choice)
    result_label.config(text=f"Your choice: {choice}\nComputer's choice: {computer_choice}\n{result}")

    if "win" in result:
        user_score += 1
    elif "lose" in result:
        computer_score += 1

    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def play_again():
    global user_score, computer_score
    answer = messagebox.askyesno("Play Again", "Do you want to play another round?")
    if answer:
        user_score = 0
        computer_score = 0
        user_score_label.config(text=f"Your Score: {user_score}")
        computer_score_label.config(text=f"Computer Score: {computer_score}")
        result_label.config(text="Choose your option...")
    else:
        root.quit()

root = tk.Tk()
root.title("Rock Paper Scissors Game")

user_score = 0
computer_score = 0

result_label = tk.Label(root, text="Choose your option...", font=('Helvetica', 14))
result_label.pack(pady=20)

user_score_label = tk.Label(root, text=f"Your Score: {user_score}", font=('Helvetica', 12))
user_score_label.pack()

computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}", font=('Helvetica', 12))
computer_score_label.pack()

rock_button = tk.Button(root, text="Rock", width=15, command=lambda: player_choice('rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=15, command=lambda: player_choice('paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: player_choice('scissors'))
scissors_button.pack(pady=5)

play_again_button = tk.Button(root, text="Play Again", width=15, command=play_again)
play_again_button.pack(pady=20)

root.mainloop()
