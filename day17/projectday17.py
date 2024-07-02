from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for items in range(len(question_data)):
    question = Question(question_data[items]["text"], question_data[items]["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():   
    quiz.next_question()