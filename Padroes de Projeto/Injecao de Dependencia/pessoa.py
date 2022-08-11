class Pessoa:

    def __init__(self, comportamento):
        self.comportamento = comportamento
    
    # função "genérica" que executa a ação da classe passada pro construtor
    def execute(self):
        self.comportamento.acao()