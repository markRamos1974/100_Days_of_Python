from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo, outro_logo

question_bank = []
for question_item in question_data:
    text = question_item["text"]
    answer = question_item["answer"]
    new_question = Question(text, answer)

    question_bank.append(new_question)

print(logo)

quiz_game = QuizBrain(question_bank)
while quiz_game.still_has_questions():
    quiz_game.next_question()


print(outro_logo)
print(f"Your final score is {quiz_game.player_score} / {quiz_game.question_number}")