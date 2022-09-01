from Chat import Chat
from ConcreteSubject import ConcreteSubject

lp2 = ConcreteSubject("LP 2")
p = ConcreteSubject("Programação")

lara = Chat("Lara")
lp2.attach(lara)

edsom = Chat("Edsom")
lp2.attach(edsom)

joao = Chat("Joao")
p.attach(joao)

maria = Chat("Maria")
p.attach(maria)

lp2.send("Olá", lara)
p.send("Olá, mundo", maria)