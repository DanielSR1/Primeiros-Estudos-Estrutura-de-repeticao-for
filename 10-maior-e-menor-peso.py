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
