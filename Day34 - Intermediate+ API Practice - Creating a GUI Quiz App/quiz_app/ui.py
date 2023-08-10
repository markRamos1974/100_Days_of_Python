THEME_COLOR = "#375362"
from tkinter import Tk, PhotoImage, Button, Canvas, Label, messagebox

class QuizInterFace():
    
    def __init__(self, quiz_brain):

        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("QuizGame")
        self.window.config(background=THEME_COLOR, padx=20)
        self.window.eval('tk::PlaceWindow . center')

        self.user_score_display = Label(text="Score: 0", font=("Arial", 15, "bold"), foreground="white")
        self.user_score_display.config(background=THEME_COLOR)
        self.user_score_display.grid(column=1, row=0, pady=40)
        
        self.canvas = Canvas(width=300, height=250, background="white")
        self.question = self.canvas.create_text(150, 125, text=self.quiz_brain.next_question(), font=("Arial", 15, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        correct_button_image = PhotoImage(file="./images/true.png")
        wrong_button_image  = PhotoImage(file="./images/false.png")


        self.correct_button = Button(image=correct_button_image, highlightthickness=0, borderwidth=0, command=self.correct)
        self.correct_button.config(background=THEME_COLOR)
        self.correct_button.grid(column=0, row=2, padx=20, pady=20)


        self.wrong_button = Button(image=wrong_button_image, highlightthickness=0, borderwidth=0, command=self.wrong)
        self.wrong_button.config(background=THEME_COLOR)
        self.wrong_button.grid(column=1, row=2, padx=20, pady=20)
        

        self.window.mainloop()

    def next_question(self):
        def default():
            new_question = self.quiz_brain.next_question()
            self.canvas.config(background="white")
            self.canvas.itemconfig(self.question, text=new_question)
            self.correct_button["state"] = "active"
            self.wrong_button["state"] = "active"

        self.window.after(2000, func=default)
        
        
        
        
    def update_screen(self, is_answer_correct):
        print(self.quiz_brain.question_number)
      

        if is_answer_correct:
            self.canvas.config(background="green")
            self.quiz_brain.score
            self.score = self.quiz_brain.score
            self.user_score_display.config(text=f"Score: {self.score}")

        else:
            self.canvas.config(background="red")
          

        if self.quiz_brain.question_number == 10:
              
            print("You've completed the quiz")
            print(f"Your final score was: {self.quiz_brain.score}/{self.quiz_brain.question_number}")
            messagebox.showinfo(title="Quiz Completed", message=f"You've completed the quiz\nyour final score was: {self.quiz_brain.score}/{self.quiz_brain.question_number}")

            self.quiz_brain.reset_game()
            self.user_score_display.config(text="Score: 0")
            self.next_question()
        else:
            self.next_question()

    
    
    def correct(self):
        is_answer_correct = self.quiz_brain.check_answer("true")
        self.correct_button["state"] = "disable"
        self.wrong_button["state"] = "disabled"
        self.update_screen(is_answer_correct)
        
        

    def wrong(self):
        is_answer_correct = self.quiz_brain.check_answer("false")
        self.correct_button["state"] = "disabled"
        self.wrong_button["state"] = "disabled"
        self.update_screen(is_answer_correct)
        


