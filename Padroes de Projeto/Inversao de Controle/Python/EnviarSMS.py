from Enviar import Enviar

class EnviarSMS(Enviar):
    def execute(user):
        print("SMS enviado com sucesso!")
        print(f"Nome: {user.nome}")
        print(f"Telefone: {user.telefone}")