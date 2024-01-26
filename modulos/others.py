import numpy as np
import random as rd

LISTA = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(LISTA)

valor_inteiro = rd.randint(20, 40)
print('\n', valor_inteiro)

ponto_flutuante = rd.random()
print(f'\nNúmero gerado: {round(ponto_flutuante * 10, 2)}')

print('\nNúmero gerado:', round(rd.uniform(1, 100), 3))
