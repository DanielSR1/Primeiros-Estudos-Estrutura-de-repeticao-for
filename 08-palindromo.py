from operator import inv
frase=str(input('Digite a frase: ')). strip().upper()
palavra=frase.split()
junto=''.join(palavra)
inverso=''
for letra in range(len(junto)-1, -1, -1):
    inverso+=junto[letra]
if inverso==junto:
    print('A frase é um PALINDROMO.')
    print(f'o inverso de {frase} é {inverso}')
else:
    print=('A frase NÃE É um PALINDROMO.')