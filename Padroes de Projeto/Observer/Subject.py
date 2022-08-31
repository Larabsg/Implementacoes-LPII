from abc import ABC, abstractmethod

class Subject(ABC):

    @abstractmethod
    def attach(self, observer):
        pass

    def detach(self, observer):
        pass

    def notify(self, message, sender):
        pass