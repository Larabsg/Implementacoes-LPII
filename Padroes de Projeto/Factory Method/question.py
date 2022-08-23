class Question:
    def __init__(self, texto, level, tag, answer):
        self.__texto = texto
        self.__level = level
        self.__tag = tag
        self.__answer = answer

    def criar(self, texto, level, tag, answer):
        return Question(texto, level, tag, answer)

    # def valida(self):
    #     if self.__texto is None or not self.__texto:
    #         raise Exception("")
    