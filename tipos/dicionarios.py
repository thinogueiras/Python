elemento = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(elemento.values())

print(f'\nElemento: {elemento["nome"]}')

print(f'\nO dicionário possui {len(elemento)} elementos\n')

elemento['grupo'] = 'Alcalinos'

print(elemento)

elemento['periodo'] = 1
print(f'\nPeríodo: {elemento["periodo"]}')

del elemento['periodo']

print(f'\n{elemento}\n')

print(elemento.items(), '\n')

for items in elemento.items():
    print(f'{items}')

print('\n')

for key in elemento.keys():
    print(f'{key}')

print('\n')

for x, y in elemento.items():
    print(f'{x}: {y}')
