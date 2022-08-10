import time
import numpy as np
 
numero = int(input())
 
ini = time.time()
 

# n = np.arange(1, numero+1)
# print(f'{n}\n{n*n}\n{n*n*n}')

for x in range(1, numero+1):
    print(f"{x} {x*x} {x*x*x}")
 
fim = time.time()
 
print(f'Tempo: {fim-ini}')