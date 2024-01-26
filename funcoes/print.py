print('Imprime a mensagem e muda de linha')
print('Imprime a mensagem e permanece na mesma linha. ', end='')
print('Continuo na mesma linha')

nome = 'Maria'
idade = 30

msg_formatada = '\nO nome dela é {0} e possui {1} anos'.format(nome, idade)
print(msg_formatada)

print('\nO nome dela é {0} e possui {1} anos'.format(nome, idade))

nome = 'Thiago'
altura = 1.76

print(f'\nOlá, meu nome é {nome} e tenho {altura}m de altura.')

a = 10
b = 15

print(f'\nA soma de {a} com {b} é igual a: {a+b}')

valor = 125.55869
print(f'\nO valor é \'{valor:.2f}\'')

nome = 'José'
idade = 30
print(f'\nNome: {nome}\tIdade: {idade}')

print('\nPyhton ' * 3)
