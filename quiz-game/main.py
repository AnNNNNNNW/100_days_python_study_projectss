from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from quiz_brain import QuizBrain

question_bank = []

for question_item in question_data:
    text = question_item["text"]
    answer = question_item["answer"]
    new_q = Question(q_text = text, q_answer = answer)
    question_bank.append(new_q)

total = len(question_data)
count = 0
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")