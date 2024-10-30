from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []
for question in question_data:
    qText = question["text"]
    qAnswer = question["answer"]
    NewQuestion = Question(qText, qAnswer)
    questionBank.append(NewQuestion)

Quiz = QuizBrain(questionBank)
#If Quiz still has questions remaining
while Quiz.stillQuestions():
    Quiz.nextQuestion()

print("You've completed the quiz!")
print(f"Your final score was: {Quiz.score}/{Quiz.questionNumber}")
