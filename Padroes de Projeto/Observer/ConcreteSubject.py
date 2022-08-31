from Subject import Subject

class ConcreteSubject(Subject):

    def __init__(self, subject):
        self.subject = subject

    _observer = []
    _state = False

    def attach(self, observer):
        print(f"{self.subject}: Adicionando {observer.nome}...")
        self._observer.append(observer)

    def detach(self, observer):
        print(f"{self.subject}: Removendo {observer.nome}...")
        self._observer.remove(observer)

    def notify(self, message, sender):
        print(f"{self.subject}: Notificando usuários...")

        for observer in self._observer:
            observer.update(self, message, sender)

    def send(self, message, sender):
        print(f"Enviando mensagem de {sender.nome}...")
        self._state = True
        self.notify(message, sender)