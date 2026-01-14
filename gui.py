import tkinter as tk
from game_logic import get_computer_choice, determine_winner

class RPSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Piatră-Hârtie-Foarfecă")

        tk.Label(root, font=("Times New Roman", 14), text="Alege o opțiune:").pack(pady=10)

        frame = tk.Frame(root)
        frame.pack()

        tk.Button(frame, text="Piatră", font=("Times New Roman", 14), command=lambda: self.play("piatra")).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Hârtie", font=("Times New Roman", 14), command=lambda: self.play("hartie")).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Foarfecă", font=("Times New Roman", 14), command=lambda: self.play("foarfeca")).grid(row=0, column=2, padx=5)

        self.result_label = tk.Label(root, text="", font=("Times New Roman", 14))
        self.result_label.pack(pady=20)

    def play(self, user_choice):
        computer = get_computer_choice()
        winner = determine_winner(user_choice, computer)

        text = f"Tu: {user_choice} | Calculator: {computer}\n"

        if winner == "egal":
            text += "Rezultat: Egalitate!"
        elif winner == "user":
            text += "Rezultat: Ai câștigat!"
        else:
            text += "Rezultat: Ai pierdut!"

        self.result_label.config(text=text)
