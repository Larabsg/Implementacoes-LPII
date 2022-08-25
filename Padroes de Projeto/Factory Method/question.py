from answer import Answer
from enum import Enum



class Question:

    class Level(Enum):
        EASY = 25
        MEDIUM = 50
        HARD = 75
        VERY_HARD = 100

        def __init__(self, score):
            self.score = score
        
        def score(self):
            return self.score

    def __init__(self, texto, level: Level, tag, answer: Answer):
        self.__texto = texto
        self.__level = level
        self.__tag = tag
        self.__answer = answer
    
    def texto(self):
        return self.__texto
    
    def level(self):
        return self.__level
    
    def tag(self):
        return self.__tag
    
    def answer(self):
        return self.__answer
    
    
