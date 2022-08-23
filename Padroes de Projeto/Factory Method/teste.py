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

class Logistica:
    def createAnswer(self):
        pass
    
    def planCreation(self):
        answer = self.createAnswer()

        result = f"Logistics: Questão criada...\n{answer.resposta()}"

        return result

class Answer(ABC): # interface comum aos vários tipos de resposta
    @abstractmethod
    def resposta(self):
        pass

class AnswerOptionsCreate(Logistica): # factory de respostas com opção
    def createAnswer(self):
        return AnswerOptions(["Lara", "Edsom", "Julia"])

class AnswerTextCreate(Logistica): # factory de respostas de texto
    def createAnswer(self):
        return AnswerText("Texto")

class AnswerOptions(Answer): 
    def __init__(self, opcoes):
        self.opcoes = opcoes

    def resposta(self):
        print(self.opcoes)
        return "Resposta de opções criada"

class AnswerText(Answer):
    def __init__(self, texto):
        self.texto = texto

    def resposta(self):
        return "Resposta de texto criada"

def client_code(logistica: Logistica):
  print(f"App: Carregado com {logistica.__class__.__name__}.",
        f"{logistica.planCreation()}")

if __name__ == "__main__":
  client_code(AnswerOptionsCreate())
  q = Question.createQuestion("P1", 15, "#historia", AnswerOptionsCreate())
  q.ver()
  print("\n")
#   client_code(AnswerTextCreate())
