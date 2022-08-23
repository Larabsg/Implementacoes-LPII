from abc import abstractmethod, ABC

class Enviar(ABC):
    @abstractmethod
    def execute(self, user):
        pass