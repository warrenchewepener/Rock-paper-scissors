import tkinter as tk
from tkinter import messagebox
import random


# Function to determine winner
def determine_winner(human_input):
    global human, computer
    computer_pick = random.choice(options)

    result = ""

    if human_input == computer_pick:
        result = "It's a tie!"
    elif (human_input == "rock" and computer_pick == "scissors") or \
         (human_input == "paper" and computer_pick == "rock") or \
         (human_input == "scissors" and computer_pick == "paper"):
        result = "Congratulations you won!"
        human += 1
    else:
        result = "Sorry you lost!"
        computer += 1

    messagebox.showinfo("Result", f"Computer picked {computer_pick}\n{result}")

# Tkinter GUI
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Assign variables as zero
human = 0
computer = 0

# Create a list
options = ["rock", "paper", "scissors"]

# Function to handle user input
def play_game(choice):
    if choice == "Quit":
        root.destroy()
    else:
        determine_winner(choice)

# Create buttons
buttons_frame = tk.Frame(root)
buttons_frame.pack()

for option in options:
    button = tk.Button(buttons_frame, text=option.capitalize(),
                       command=lambda o=option: play_game(o))
    button.pack(side="left", padx=10, pady=10)

quit_button = tk.Button(buttons_frame, text="Quit", command=lambda: play_game("Quit"))
quit_button.pack(side="left", padx=10, pady=10)

root.mainloop()

# Print game summary
print(f"Well done you won {human} times")
print(f"The computer won {computer} times")
print("Goodbye!")
