"""5. Faça um programa para a leitura de duas notas parciais de 
um aluno. O programa deve calcular a média alcançada por 
aluno e apresentar: - A mensagem "Aprovado", se a média alcançada for maior ou 
igual a sete; - A mensagem "Reprovado", se a média for menor do que sete; - A mensagem "Aprovado com Distinção", se a média for igual 
a dez. """

n1 = float(input('Digite sua 1º nota ==>'))
n2 = float(input('Digite sua 2º nota ==>'))
soma = (n1 + n2)/2

if soma == 10:
    print(f'Aprovado com Distinção - média :{soma}')
elif soma >= 7:
    print(f'Aprovado - média :{soma}')
else:
    print(f'Reprovado - média :{soma}')