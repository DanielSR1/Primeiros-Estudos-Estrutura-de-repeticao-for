#nesse exercicio desenvolvi um programa capaz de ler o nome, idade e sexo de 4 pessoas. No final do programa, mostra: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade=0
maioridadehomem=0
nomevelho=''
maioridade=0
contamulher20=0
for c in range(1,5):
    print(f'---- {c}° pessoa----')
    nome=str(input('Nome:'))
    idade=int(input('Idade:'))
    sexo=str(input('[M/F]'))
    somaidade=somaidade+idade
    if c==1 and sexo in"Mm":
        maioridadehomem=idade
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridade=idade
        nomevelho=nome
    if sexo in 'Ff' and idade<20:
        totmulher=contamulher20+1
mediaidade=somaidade/4
print(f'A média de idade do grupo é {mediaidade}')
print(f'O nome do Homem mais velho é {nomevelho}')
print(f'O número de mulheres com menos de VINTE anos é {totmulher}')



