# São imutáveis

tupla_1 = (1, 2, 1, 2, 3, 2, 4, 5, 3, 1, 2, 5, 4, 3, 2)

print('Soma de todos os números da tupla:', sum(tupla_1))

print('Qtde de números 1:', tupla_1.count(1))
print('Qtde de números 2:', tupla_1.count(2))
print('Qtde de números 3:', tupla_1.count(3))
print('Qtde de números 4:', tupla_1.count(4))
print('Qtde de números 5:', tupla_1.count(5))
print('Qtde de números 10:', tupla_1.count(10))

tupla_2 = ('João', 'José', 'Maria', 'Thiago', 'Joana', 'Raquel')

print(tupla_2[0: 2])  # João e José
print(tupla_2[2: 3])  # Maria
print(tupla_2[1: 2])  # José
print(tupla_2[-1])  # Raquel
print(tupla_2[:3])  # João, José e Maria
print(tupla_2[3:5])  # Thiago e Joana

print('Joaquin' in tupla_2)  # False

lista = list(tupla_2)
print('\n', lista)
