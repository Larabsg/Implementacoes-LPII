import time
from unittest import result
import numpy as np
 
#usando a característica do input (captura de tela), para receber o número inteiro que o usuário digitar
numero = int(input("fatorial de: "))
inicio = time.time()
 
#resultado, cont = 1,1
#while cont<= numero:
  #  resultado *= cont
  #  cont += 1
#for n in range(1, numero+1):
#    resultado *= n
    
#usando a biblioteca do numpy para calcular o número fatorial
resultado = np.math.factorial(numero)
 
#exibe o resultado
print(resultado)
fim = time.time()
 
#exibe o tempo de execução
print("tempo: ", fim - inicio)