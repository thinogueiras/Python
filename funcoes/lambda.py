from functools import reduce


def quadrado(x): return x**2


for i in range(1, 11):
    print(quadrado(i))

print('\n')


def par(x): return x % 2 == 0


print(par(4))
print(par(5))

print('\n')

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

dobro = list(map(lambda x: x * 2, lista_numeros))

print(dobro)

print('\n')

palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
maiusculas = list(map(str.upper, palavras))
# maiusculas = list(map(lambda x: x.upper(), palavras))

print(maiusculas)

print('\n')


def numeros_pares(num):
    return num % 2 == 0


num_pares = tuple(filter(numeros_pares, lista_numeros))
print(f'Números pares filtrados da lista: {num_pares}')

num_impares = set(filter(lambda x: x % 2 != 0, lista_numeros))
print(f'Números ímpares filtrados da lista: {num_impares}')

print('\n')


def mult(x, y):
    return x * y


numeros = [1, 2, 3, 4]

total = reduce(mult, numeros)
print(total)

total = reduce(lambda x, y: x**2 + y**2, numeros) # ((1² + 2²)² + 3²)² + 4² 
print(total)
