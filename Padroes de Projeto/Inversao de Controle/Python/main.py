from EnviarEmail import EnviarEmail
from EnviarSMS import EnviarSMS
from Usuario import Usuario
from CadastrarUsuario import CadastrarUsuario

user = Usuario.criar("Lara", "lara@gmail.com", "88 1111 1111")

CadastrarUsuario.cadastro(user, EnviarEmail)