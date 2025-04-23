from data import questions_aot
from question_model import Question
from quiz_brain import QuizBrain
from questions_sl import questions_solo_leveling
from questions_bl import questions_blue_lock
choice = int(input('''
1 - Attack on Titan
2 - Solo Leveling
3 - Blue lock
: '''))
if choice == 1:
   qs = questions_aot
elif choice == 2:
   qs = questions_solo_leveling
elif choice == 3:
   qs = questions_blue_lock
else:
   print("Default questions are from 1 - AOT.")
   qs = questions_aot
question_bank = []
for item in qs:
   question = item["question"]
   answer = item["answer"]
   new_question = Question(question,answer) ## created a
   question_bank.append(new_question) ##
# print(question_bank[10].text) ##

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
   quiz.next_question()
   quiz.check_answer()
print("You've completed the quiz.")
print(f"The final score is {quiz.score}/12.")