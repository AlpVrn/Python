#Question
class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer == answer

#Quiz
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    def loadQuestion(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()
    def displayQuestion(self):
        Question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {Question.text}')

        for  q in Question.choices:
            print('-' + q)
        
        answer = input('Cevap : ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        Question = self.getQuestion()

        if Question.checkAnswer(answer):
            self.score +=1
        self.questionIndex+=1

        self.displayQuestion()

    

    def showScore(self):
        pass
q1=Question('En iyi programlama dili hangisidir ?',['C#','Python','Javascript','java'],'Python')
q2=Question('En popüler programlama dili hangisidir ?',['C#','java','Javascript','Python'],'Python')
q3=Question('En çok kazandıran programlama dili hangisidir ?',['C#','Javascript','Python','java'],'Python')
questions=[q1,q2,q3]


quiz = Quiz(questions)

quiz.displayQuestion()
