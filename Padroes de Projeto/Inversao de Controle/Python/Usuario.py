from wsgiref import validate


class Usuario:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

        self.validated()
    
    def criar(nome, email, telefone):
        return Usuario(nome, email, telefone)
    
    def validated(self):
        if self.nome is None or not self.nome:
            raise Exception("Nome é obrigatório!")
        if self.email is None or not self.email:
            raise Exception("Email é obrigatório!")
        if self.telefone is None or not self.telefone:
            raise Exception("Telefone é obrigatório!")
    
    def update(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

        self.validated()
    
    def nome(self):
        return self.nome

    def email(self):
        return self.email

    def telefone(self):
        return self.telefone
    