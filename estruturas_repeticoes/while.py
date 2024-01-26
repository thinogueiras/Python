num = 1

while num <= 10:
    print(f'ORDEM CRESCENTE: {num}')
    num += 1
print('\nLaço crescente encerrado')

#########################################################################
print('\n#########################################################################')

num = 10

while num >= 1:
    print(f'ORDEM DECRESCENTE: {num}')
    num -= 1
print('\nLaço decrescente encerrado')

#########################################################################
print('\n#########################################################################')

nome = None

while True:
    nome = input('\nDigite o seu nome, ou X para parar: ')
    if nome == 'x' or nome == 'X':
        break
    print(f'\nBem-vindo, {nome} \n')
print('\nAté logo!!!')
