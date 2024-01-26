frase = 'Vamos aprender Pyhton hoje'

palavras = frase.split()
print(palavras)

for palavra in palavras:
    print(f'{palavra.upper()} ==> tamanho da palavra:', len(palavra))

email = 'thiago.nogueira@qa-automation.com.br'

arroba = email.find('@')

user = email[0: arroba]
dominio = email[arroba + 1:]

print(f'\nUser: {user}')
print(f'Domínio: {dominio}')

nome = 'T h I a G o'

novo_nome = nome.replace(' ', '').upper()
print(f'\n{novo_nome}')
