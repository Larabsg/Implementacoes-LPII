from Cadastro import Cadastro
from Mensage import *


resposta = int(input("1- Email\n2- SMS\n3- Zap\n"))

if resposta == 1:
    user = Cadastro("Lara", Mensage.email)
elif resposta == 2:
    user = Cadastro("Lara", Mensage.sms)
else:
    user = Cadastro("Lara", Mensage.zap)