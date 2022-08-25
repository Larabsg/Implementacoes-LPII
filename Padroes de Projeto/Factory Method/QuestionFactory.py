from Question import Question
from AnswerText import AnswerText
from AnswerChoice import AnswerChoice

class QuestionFactory:

    def createAnswerText(texto, level: Question.Level, tag):
        return Question(texto, level, tag, AnswerText())

    def createAnswerChoice(texto, level: Question.Level, tag, options):
        return Question(texto, level, tag, AnswerChoice(options))