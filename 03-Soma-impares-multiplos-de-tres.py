#NESSE EXERCICIOS  DESENVOLVI um programa que calculA a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma=0
conta=0
for c in range (1,501,2):
    if c%3==0:
        conta=conta+1
        soma=soma+c
print(f'A soma de todos os {conta} valores é {soma}')
