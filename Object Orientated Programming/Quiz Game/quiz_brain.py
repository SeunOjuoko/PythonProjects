class QuizBrain:
    def __init__(self, qList):
        self.questionNumber = 0
        self.questionlist = qList
        self.score = 0

    def stillQuestions(self):
        #return self.questionNumber < len(self.question_list):
        if self.questionNumber < len(self.questionlist):
            return True
        else:
            return False

    def nextQuestion(self):
        currentQuestion = self.questionlist[self.questionNumber]
        self.questionNumber += 1
        answer = input(f"Q.{self.questionNumber}: {currentQuestion.text} (True/False): ")
        self.checkAnswer(answer,currentQuestion.answer)

    def checkAnswer(self, answer, correctAnswer):
        if answer == correctAnswer:
            print("CORRECT!!!")
            self.score += 1
        else:
            print("INCORRECT!!!")
        print(f"Your score is {self.score} out of {self.questionNumber}")
        print(f"The answer is {correctAnswer}")
        print(" \n")

