import random

for contador_externo in range(1, 6):
    print(f'\nRodada: {contador_externo}')
    for contador_interno in range(5, 0, -1):
        print(f'Valor: {contador_interno}')

print('\nFim dos laços de repetições')

#########################################################################
print('\n#########################################################################')

for A in range(1, 6):
    print(f'\nConjunto {A}')
    for B in range(6):
        numero = random.randint(1, 61)
        print(f'Valor: {numero}')
