"""3. Faça um Programa que verifique se uma letra digitada é 
"F" ou "M". Conforme a letra escrever: F - Feminino, M - 
Masculino, Sexo Inválido. """
sexo = input('Digite seu sexo (F ou M):').strip().lower()
if sexo == 'f':
    print('Feminino')
elif sexo == 'm':
    print('Masculino')
else:
    print('Entrada inválida')
