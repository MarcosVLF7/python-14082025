"""4. Faça um Programa que verifique se uma letra digitada é 
vogal ou consoante. """

letra = input('Digite uma letra ==>').lower().strip()
if letra == 'a' or letra == 'e' or letra =='i' or letra == 'o' or letra == 'u':
    print(f'Você digitou uma vogal => {letra}')
else:
    print(f'Você digitou uma consoante => {letra}')