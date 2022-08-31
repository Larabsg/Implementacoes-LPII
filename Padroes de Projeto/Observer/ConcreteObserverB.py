from Observer import Observer

class ConcreteObserverB(Observer):

    def __init__(self, nome):
        self.nome = nome

    def update(self, subject, message, sender):
        if subject._state == True and not isinstance(sender, ConcreteObserverB):
            print(f"{self.nome}: Recebi mensagem de {sender.nome}")
            print(f"{sender.nome} diz: {message}")