import tkinter as tk
from tkinter import messagebox

class TriviaGUI:
    def __init__(self, master, questions):
        self.master = master
        self.master.title("Trivia Challenge")
        self.questions = questions
        self.index = 0
        self.score = 0
        self.correct_answer = ""
        self.selected_answer = tk.IntVar()

        self.question_label = tk.Label(master, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=10)

        # Frame để chứa các đáp án, và căn giữa
        self.answer_frame = tk.Frame(master)
        self.answer_frame.pack(pady=5)

        self.radio_buttons = []
        for i in range(3):
            rb = tk.Radiobutton(
                self.answer_frame,
                text="",
                variable=self.selected_answer,
                value=i,
                font=("Arial", 12),
                anchor="w",
                justify="left"
            )
            rb.pack(anchor="center", pady=2)
            self.radio_buttons.append(rb)

        self.submit_button = tk.Button(master, text="Nộp", command=self.submit_answer)
        self.submit_button.pack(pady=5)

        self.score_label = tk.Label(master, text="Điểm: 0", font=("Arial", 12))
        self.score_label.pack()

        self.end_button = tk.Button(master, text="Kết thúc", command=self.end_game)
        self.end_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.index < len(self.questions):
            q, a_list, correct = self.questions[self.index]
            self.correct_answer = a_list[correct - 1].strip().lower()
            self.question_label.config(text=q)
            self.selected_answer.set(-1)
            for i in range(3):
                self.radio_buttons[i].config(text=f"{chr(65+i)}. {a_list[i]}")
        else:
            self.end_game()

    def submit_answer(self):
        choice = self.selected_answer.get()
        if choice == -1:
            messagebox.showwarning("Cảnh báo", "Hãy chọn một đáp án trước khi nộp.")
            return

        chosen_text = self.radio_buttons[choice].cget("text").split(". ", 1)[1].strip().lower()
        if chosen_text == self.correct_answer:
            self.score += 1
            messagebox.showinfo("Kết quả", "✅ Đúng!")
        else:
            messagebox.showinfo("Kết quả", f"❌ Sai!\nĐáp án đúng: {self.correct_answer.capitalize()}")
        self.score_label.config(text=f"Điểm: {self.score}")
        self.index += 1
        self.master.after(1500, self.load_question)

    def end_game(self):
        messagebox.showinfo("Kết thúc", f"Tổng điểm: {self.score}")
        self.master.quit()
