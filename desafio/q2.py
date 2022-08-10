import time
import numpy as np

def div(numero):
    for i in range(1,numero+1):
        if numero % i == 0:
            print(i)
 
def divisor(numero):
    n = np.arange(1,numero+1) # o 1 é o start do range
    d = numero % n          # calculando o resto
    resto = d == 0            # atribuindo o valor do resto, caso for igual a zero 
    print(n[resto], numero) # printando o array quando o índice for true

inicio = time.time()  
divisor(100888886)
fim = time.time()
print('Tempo:', (fim-inicio)/1000)
