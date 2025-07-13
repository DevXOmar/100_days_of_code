import tkinter as tk
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self,quizbrain:QuizBrain): ## tells us that the quizbrain param must be an instance of the QuizBrain class.
        self.quiz = quizbrain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.minsize(width= 200,height=200)
        self.window.config(padx = 20,pady = 20,bg=THEME_COLOR)

        self.img1 = tk.PhotoImage(file="images/true.png")
        self.right_button = tk.Button(image=self.img1,highlightthickness=0,command= self.correct_pressed)
        self.right_button.grid(row=2, column=1)

        self.img2 = tk.PhotoImage(file="images/false.png")
        self.wrong_button = tk.Button(image=self.img2,highlightthickness=0,command= self.wrong_pressed) ##.
        self.wrong_button.grid(row=2, column=0)

        self.canvas3 = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas3.create_text(150, 130, text="Some questions", fill=THEME_COLOR, font = ("Arial",20,"italic"),width = 280)
        self.canvas3.grid(row=1, column=0, columnspan=2)

        self.score_label = tk.Label(text = "Score : 0",fg = "white")
        self.score_label.grid(row = 0, column = 1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas3.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas3.itemconfig(self.question_text,text = q_text)
        else:
            self.canvas3.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.right_button.config(state = "disabled")
            self.wrong_button.config(state = "disabled")

    def correct_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def wrong_pressed(self):
        is_wrong = self.quiz.check_answer("False")
        self.give_feedback(is_wrong)
    def give_feedback(self,is_ans):
        if is_ans:
           self.canvas3.config(bg="green")
        else:
            self.canvas3.config(bg = "red")
        self.window.after(1000,self.get_next_question)