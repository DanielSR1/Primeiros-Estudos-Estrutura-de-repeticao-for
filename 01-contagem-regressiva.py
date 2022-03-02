#NESSE EXERCICIO FOI DESENVOLVIDO UM PROGRAMA CAPAZ DE FAZER UMA CONTAGEM REGRESSIVA DE 10 A 0.
from time import sleep
print('\033[33mCONTEGEM REGRESSIVA!!\033[m')
for c in range(10, -1,-1):
    print(c)
    sleep(1)
print('FIM!!')