from pessoa import Pessoa
from correr import Correr
from falar import Falar

pessoa1 = Pessoa(Correr())
pessoa1.execute()

pessoa2 = Pessoa(Falar())
pessoa2.execute()