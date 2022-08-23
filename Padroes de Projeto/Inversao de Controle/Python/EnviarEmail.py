from Enviar import Enviar

class EnviarEmail(Enviar):

    def execute(user):
            print("Email enviado com sucesso!")
            print(f"Nome: {user.nome}")
            print(f"Email: {user.email}")