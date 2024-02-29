import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Game")
        self.root.geometry("400x300")

        self.questions = [
            ("What is the capital of France?", ["Paris", "Berlin", "London", "Rome"], 1),
            ("Which planet is known as the Red Planet?", ["Jupiter", "Mars", "Saturn", "Venus"], 2),
            ("What is 7 + 3?", ["8", "9", "10", "11"], 3),
        ]
        self.question_number = 0
        self.score = 0

        self.question_text = tk.StringVar()
        self.question_label = tk.Label(root, textvariable=self.question_text, wraplength=300)
        self.question_label.pack(pady=10)

        self.radio_var = tk.IntVar()
        self.radio_buttons = []
        for i in range(4):
            radio = tk.Radiobutton(root, text="", variable=self.radio_var, value=i+1)
            self.radio_buttons.append(radio)
            radio.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.display_question()

    def display_question(self):
        self.radio_var.set(-1)  # Deselect all radio buttons

        question, options, _ = self.questions[self.question_number]
        self.question_text.set(question)
        for i in range(4):
            self.radio_buttons[i].config(text=options[i])

    def next_question(self):
        user_answer = self.radio_var.get()
        correct_answer = self.questions[self.question_number][2]
        if user_answer == correct_answer:
            self.score += 1

        self.question_number += 1
        if self.question_number < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Complete", f"Quiz complete! Your score is: {self.score}/{len(self.questions)}")
        self.root.destroy()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
