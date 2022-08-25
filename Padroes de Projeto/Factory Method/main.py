from AnswerText import AnswerText
from AnswerChoice import AnswerChoice
from QuestionFactory import QuestionFactory
from Question import Question

question = QuestionFactory.createAnswerChoice("Quem descobriu o brasil?", 
                                                Question.Level.EASY,
                                                "#historia",
                                                ["Pedro", "João", "José"]
                                            )

question2 = QuestionFactory.createAnswerText("Questão 2",
                                                Question.Level.VERY_HARD,
                                                "#variado"
                                                )

print(f"{question.texto()}\nTipo: {question.level().value}\n")
print(f"{question2.texto()}\nTipo: {question2.level().value}")