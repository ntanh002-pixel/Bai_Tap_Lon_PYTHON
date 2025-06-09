# main.py

from file_handler import open_file
from trivia_gui import TriviaGUI
import tkinter as tk

def main():
    filename = "question_file.txt"
    try:
        questions = open_file(filename)
        root = tk.Tk()
        app = TriviaGUI(root, questions)
        root.mainloop()
    except Exception as e:
        print("Lỗi:", e)

if __name__ == "__main__":
    main()
