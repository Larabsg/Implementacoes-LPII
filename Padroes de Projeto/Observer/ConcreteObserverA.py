from Observer import Observer

class ConcreteObserverA(Observer):

    def __init__(self, nome):
        self.nome = nome

    def update(self, subject, message, sender):
        if subject._state == True and not isinstance(sender, ConcreteObserverA):
            print(f"{self.nome}: Recebi mensagem de {sender.nome}")
            print(f"{sender.nome} diz: {message}")