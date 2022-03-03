#NESSE EXERCICIOS DESENVOLVI UM PROGRAMA CAPAZ DE DIZER QUAL A TABUDADE DE 1 A 10 DO NÚMERO ESOLHIDO.
nu=int(input('Digite um número para ver a tabuada: '))
for v in range(1, 11):
    r=nu*v
    print(f'\033[32m{nu} x {v}= {r} ')

