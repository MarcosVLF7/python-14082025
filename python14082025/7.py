"""7. Faça um Programa que leia três números e mostre o maior e 
o menor deles. """

n1 = float(input('Digite um número ==>'))
n2 = float(input('Digite um número ==>'))
n3 = float(input('Digite um número ==>'))

if n1 > n2 and n1 > n3:
    print(f'{n1} é maior do que {n2} e {n3}')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é maior do que {n1} e {n3}')
elif n3 > n1 and n3 > n2:
    print(f'{n3} é maior do que {n1} e {n2}')
if n1 < n2 and n1 < n3:
    print(f'{n1} é menor do que {n2} e {n3}')
if n2 < n1 and n2 < n3:
    print(f'{n1} é menor do que {n2} e {n3}')
if n3 < n1 and n3 < n2:
    print(f'{n1} é menor do que {n2} e {n3}')
else:
    print(f'Números iguais ou Entrada inválida!')