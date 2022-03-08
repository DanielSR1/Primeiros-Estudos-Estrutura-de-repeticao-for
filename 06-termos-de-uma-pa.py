print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
nu=int(input('Primeiro termo: '))
r=int(input('Razão: '))
de= nu+(10-1)* r
for pa in range(nu,de+r,r):
    print(f'{pa}', end=' -> ')
