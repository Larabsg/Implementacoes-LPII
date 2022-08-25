from abc import abstractmethod, ABC

class Answer(ABC):
    
    @abstractmethod
    def type(self):
        pass