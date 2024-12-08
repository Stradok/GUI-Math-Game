# mathgame_LastName_FirstName.py
# Program Description: A GUI-based Math Game for kids to learn multiplication tables using quizzes and flashcards.
# Author: [Your Name]
# Date: [Today's Date]

import tkinter as tk
from tkinter import messagebox, LabelFrame, Frame
import random

class MathGame:
    def __init__(self):
        # Initialize the main window
        self.window = tk.Tk()
        self.window.title("Math Game")
        
        # Variables
        self.mode = tk.StringVar(value="Quiz")
        self.num1 = 0
        self.num2 = 0
        self.user_answer = tk.StringVar()
        self.answer_message = tk.StringVar()
        
        # Layout Widgets
        self.create_widgets()
        self.generate_question()
        
        # Start the application
        self.window.mainloop()

    def create_widgets(self):
        # Mode Selector
        mode_frame = LabelFrame(self.window, text="Mode", padx=10, pady=10)
        mode_frame.pack(pady=10)
        tk.Radiobutton(mode_frame, text="Quiz", variable=self.mode, value="Quiz", command=self.process_mode).pack(side="left", padx=5)
        tk.Radiobutton(mode_frame, text="FlashCard", variable=self.mode, value="FlashCard", command=self.process_mode).pack(side="left", padx=5)

        # Question and Answer Widgets
        self.question_label = tk.Label(self.window, text="", font=("Arial", 16))
        self.question_label.pack(pady=10)
        
        self.answer_label = tk.Label(self.window, text="", font=("Arial", 12), fg="green")
        self.user_answer_label = tk.Label(self.window, text="Your Answer:")
        self.answer_entry = tk.Entry(self.window, textvariable=self.user_answer)
        self.answer_entry.bind("<Return>", self.check_answer)
        
        # Buttons
        button_frame = Frame(self.window)
        button_frame.pack(pady=10)
        self.show_answer_button = tk.Button(button_frame, text="Show Answer", command=self.show_answer)
        self.next_question_button = tk.Button(button_frame, text="Next Question", command=self.next_question)
        exit_button = tk.Button(button_frame, text="Exit Game", command=self.window.destroy)
        
        # Packing Buttons
        self.show_answer_button.pack(side="left", padx=5)
        self.next_question_button.pack(side="left", padx=5)
        exit_button.pack(side="left", padx=5)

    def process_mode(self):
        if self.mode.get() == "FlashCard":
            self.answer_label.pack_forget()
            self.user_answer_label.pack_forget()
            self.answer_entry.pack_forget()
            self.show_answer_button.pack_forget()
        else:
            self.user_answer_label.pack(pady=5)
            self.answer_entry.pack(pady=5)
            self.answer_label.pack(pady=5)
            self.show_answer_button.pack(side="left", padx=5)

    def generate_question(self):
        self.num1 = random.randint(1, 9)
        self.num2 = random.randint(1, 9)
        if self.mode.get() == "FlashCard":
            self.question_label.config(text=f"{self.num1} x {self.num2} = {self.num1 * self.num2}")
        else:
            self.question_label.config(text=f"{self.num1} x {self.num2} = ?")
            self.user_answer.set("")
            self.answer_message.set("")
            self.answer_label.config(text="")

    def check_answer(self, event=None):
        try:
            user_input = int(self.user_answer.get())
            correct_answer = self.num1 * self.num2
            if user_input == correct_answer:
                self.answer_message.set("Correct!")
                self.answer_label.config(text="Correct!", fg="green")
            else:
                self.answer_message.set(f"Incorrect! The correct answer is {correct_answer}.")
                self.answer_label.config(text=f"Incorrect! The correct answer is {correct_answer}.", fg="red")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")
            self.user_answer.set("")

    def show_answer(self):
        correct_answer = self.num1 * self.num2
        self.answer_label.config(text=f"Answer: {correct_answer}", fg="blue")

    def next_question(self):
        self.generate_question()

# Run the Math Game
if __name__ == "__main__":
    MathGame()
