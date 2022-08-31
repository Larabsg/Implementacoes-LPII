from ConcreteObserverA import ConcreteObserverA
from ConcreteObserverB import ConcreteObserverB
from ConcreteSubject import ConcreteSubject

lp2 = ConcreteSubject("LP 2")

lara = ConcreteObserverA("Lara")
lp2.attach(lara)

mel = ConcreteObserverB("Melissa")
lp2.attach(mel)

lp2.send("Olá!", lara)
