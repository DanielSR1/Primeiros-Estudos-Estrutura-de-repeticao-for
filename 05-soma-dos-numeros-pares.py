#NESSE EXERCICO Desenvolvi um programa capaz de ler seis números inteiros e mostre a soma apenas daqueles que forem par. Se o valor digitado for ímpar, ele o desconsidera.
soma=0
conta=0
for v in range(1,7):
    num=int(input(f'\033[32mDigite o {v}º valor: '))
    if num%2==0:
        soma=soma+num
        conta=conta+1
print(f'\033[36mVocê informou {conta} números pares, e a soma deles foi {soma}.')





