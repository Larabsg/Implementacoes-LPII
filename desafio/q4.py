import time

N = int(input())  # Recebe o número de valores a serem analisados
in_ = 0           # Indica o número de valores presentes no intervalo
out_ = 0          # Indica o número de valores fora do intervalo

ini = time.time()

for i in range(1, N+1):
    num = int(input())
    if(num >= 10 and num <= 20):     # Condição para o intervalo [10,20]
        in_ += 1
    else:
        out_ +=1
        
fim = time.time()

print(f'{in_} in')          # Exibe a quantidade de valores 
print(f'{out_} out')        # dentro e fora do intervalo

print(f'Tempo: {(fim-ini)/1000 }')
