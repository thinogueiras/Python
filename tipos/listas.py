# São mutáveis

carros_vw = ['Gol', 'Fox', 'Polo', 'Golf', 'Jetta', 'Amarok']

for carro in carros_vw:
    print(carro.upper())

carros_gm = ['Corsa', 'Onix', 'Cruze', 'Cobalt', 'Tracker', 'S10']

print('\n')

for carro in carros_gm:
    print(carro.lower())

todos_carros = carros_vw + carros_gm

print('\nTamanho da lista:', len(todos_carros))  # 12
print('\n', sorted(todos_carros))

todos_carros.append('Fusca')
print('\nTamanho da lista:', len(todos_carros))  # 13
print('\n', sorted(todos_carros))

print('\n', 'Fusca' in todos_carros)  # True

todos_carros += 'Classic', 'Parati'
print('\nTamanho da lista:', len(todos_carros))  # 15

print('\n', todos_carros)
todos_carros.pop()  # Remove o último item da lista
print('\nTamanho da lista:', len(todos_carros))  # 14
print('\n', todos_carros)

todos_carros.insert(0, 'T-Cross')
print('\nTamanho da lista:', len(todos_carros))  # 15
print('\n', todos_carros)

print('\n')

# Compreensão de listas

numeros = [1, 2, 6, 7, 8, 12]

quadrados_1 = list(map(lambda x: x**2, numeros))
print(quadrados_1)

quadrados_2 = [num ** 2 for num in numeros]
print(quadrados_2)

print('\n')

pares = [num for num in range(11) if num % 2 == 0]
print(pares)

frase = 'A lógica é apenas o princípio da sabedoria, e não o seu fim.'
vogais = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'u', 'ú']

lista_vogais = [v for v in frase if v in vogais]
print(f'\nA frase possui {len(lista_vogais)} vogais: {lista_vogais}\n')

distributiva = [k * m for k in [2, 3, 5] for m in [10, 20, 30]]
print(distributiva)

for k in [2, 3, 5]:
    for m in [10, 20, 30]:
        print(k * m, end=' ')
