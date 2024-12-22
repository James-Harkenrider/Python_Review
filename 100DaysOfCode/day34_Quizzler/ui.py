from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", padx=20, pady=20)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic"),
            width=280
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.get_next_question()

        true_photo = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=true_photo,
            highlightthickness=0,
            command=self.true_answer
        )
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        false_photo = PhotoImage(file="./images/false.png")
        self.false_button = Button(
            image=false_photo,
            highlightthickness=0,
            command=self.false_answer
        )
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
            self.score_label.configure(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfigure(self.question_text, text="You've reached the end of the quiz.")
            self.score_label.configure(text=f"Score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)

