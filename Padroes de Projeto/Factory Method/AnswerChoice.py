from answer import Answer

class AnswerChoice(Answer):

    def __init__(self, options):
        self.options = options
    
    def getOptions(self):
        return self.options

    def type(self):
        return "CHOICE"