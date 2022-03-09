#NESSE EXERCICIO DESENVOLVI UM ALGORIIMO CAPAZ DE CONTAR QUANTAS PESSOAS EM UMA LISTA SÃO MAIORES OU MENORES DE IDADE DE ACORDO COM SUAS DATAS DE NASCIMENTO.
from datetime import date
atual= date.today().year 
maior=0
menor=0
for p in range(1,8):
    nasc=int(input(f'Em que ano a {p}°pessoa nasceu? '))
    idade=atual-nasc
    if idade> 21:
        maior=maior+1
    else:
        menor=menor+1
print(f'Nessa lista temos ao todo {maior} pessoas maiores de idade.')
print(f'Nessa lista temos ao todo {menor} pessoas menores de idade.')

