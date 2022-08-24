from abc import ABC, abstractmethod

class Question:
    def __init__(self, texto, level, tag, answer):
        self.__texto = texto
        self.__level = level
        self.__tag = tag
        self.answer = answer
    
    def createQuestion(texto, level, tag, answer):
        return Question(texto, level, tag, answer)
        
    def ver(self):
        print(self.__texto)
        print(self.__level)
        print(self.__tag)

class QuestionFactory:
    def createAnswer(self):
        pass
    
    def planCreation(self):
        answer = self.createAnswer()

        result = f"Logistics: Questão criada...\n{answer.tipo()}"

        return result

class Answer(ABC): # interface comum aos vários tipos de resposta
    @abstractmethod
    def tipo(self):
        pass

class AnswerFactory(QuestionFactory):
    pass

class AnswerOptionsCreate(QuestionFactory): # factory de respostas com opção
    def __init__(self, options):
        self.options = options
        
    def createAnswer(self):
        return AnswerOptions(self.options)

class AnswerTextCreate(QuestionFactory): # factory de respostas de texto
    def createAnswer(self):
        return AnswerText()

class AnswerOptions(Answer): 
    def __init__(self, opcoes):
        self.opcoes = opcoes
    
    def options(self):
        return self.opcoes

    def tipo(self):
        return "CHOICE"

class AnswerText(Answer):
    def tipo(self):
        return "TEXT"

def client_code(QuestionFactory: QuestionFactory):
  print(f"App: Carregado com {QuestionFactory.__class__.__name__}.",
        f"{QuestionFactory.planCreation()}")

if __name__ == "__main__":
  q = Question.createQuestion("P1", 15, "#historia", client_code(AnswerOptionsCreate(["Mell", "Mateus", "Maiko"])))
  q1 = Question.createQuestion("P2", 15, "#matematica", client_code(AnswerTextCreate()))
  print(q.answer)
  list = [q1]

  for i in list:
    print(i.ver())
    print(i.answer)




  print("\n")
