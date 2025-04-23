from logging import NullHandler


class QuizBrain:

   def __init__(self,qlist):
       self.question_number = 0
       self.question_list = qlist
       self.score = 0

   def next_question(self):
       current_question = self.question_list[self.question_number].text
       self.question_number +=1
       self.answer = input(f"Q{self.question_number}. {current_question} [True/False]:\n")

   def still_has_questions(self):
       if self.question_number < len(self.question_list) :
           return True
       else:
           return False

   def check_answer(self):
       if self.answer.lower() == self.question_list[self.question_number-1].answer.lower():
           self.score +=1
           print("You got it right!")
       else:
           print("Wrong answer!")
       print(f"score: {self.score}/{self.question_number}\n")