#NESSE EXERCICIOS DESENVOLVI UM PROGRAMA CAPAZ DE ANALISAR O PESO DE 7 PESSOAS DIFERENTES E DIZER QUAL DELAS TEM O MAIOR E O MENOR PESO.
maior=0
menor=0
for p in range(1, 6):
    peso=float(input(f'Qual o peso da {p}° pessoa? '))
    if p==1:
        maior=p
        menor=p
    else:
        if peso>maior:
            maior=peso
        if peso< menor:
            menor=peso
print(f'O maior peso é {maior}.')
print(F'O menor peso é {menor}.')
