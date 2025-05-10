import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.geometry("400x300")
app.title("Rock Paper Scissors")


title = ctk.CTkLabel(app, text="Welcome in game")
title.pack(pady=5)


result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=5)


player_wins = 0
computer_wins = 0


def play(player_choice):
    global player_wins, computer_wins
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result_label.configure(text="Draw! Both chose " + player_choice)
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        player_wins += 1
        result_label.configure(text=f"You win! Computer chose {computer_choice}")
    else:
        computer_wins += 1
        result_label.configure(text=f"You lose! Computer chose {computer_choice}")

   
    wins_label.configure(text="Wins for computer: " + str(computer_wins))
    wins_label2.configure(text="Wins for player: " + str(player_wins))




rock_btn = ctk.CTkButton(app, text="Rock", command=lambda: play("rock"))
rock_btn.pack(pady=5)

paper_btn = ctk.CTkButton(app, text="Paper", command=lambda: play("paper"))
paper_btn.pack(pady=5)

scissors_btn = ctk.CTkButton(app, text="Scissors", command=lambda: play("scissors"))
scissors_btn.pack(pady=5)

wins_label = ctk.CTkLabel(app, text="Wins for computer: " + str(computer_wins))
wins_label.pack(pady=5)

wins_label2 = ctk.CTkLabel(app, text="Wins for player: " + str(player_wins))
wins_label2.pack(pady=5)

wins_label.configure(text="Wins for computer: " + str(computer_wins))
wins_label2.configure(text="Wins for player: " + str(player_wins))

app.mainloop()
