#NESSE EXERCICIO DESENVOLVI UM PROGRAMA CAPAZ DE DIZER SE UM NÚMERO É OU NÃO UM NÚMERO PRIMO.
from os import readlink
contador=0
nu=int(input('Digite um número: '))
for d in range(1, nu + 1):
    if nu % d==0:
        print('\033[33m', end=' ')
        print(f'{d}', end=' ')
        contador=contador+1
    else:
        print('\033[31m', end=' ')
        print(f'{d}', end=' ')
print(f'\n\033[34m{nu} foi divisivel {contador} vezes.\033[m')
if contador==2:
    print(f'\033[32m{nu} é um número primo.')
else:
    print(f'\033[31m{nu} não é um número primo.')
      