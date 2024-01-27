bebidas = ['Café', 'Chá', 'Cerveja', 'Chopp', 'Cachaça']

for i, item in enumerate(bebidas):
    print(f'\nÍndice: {i + 1}, Item: {item}')

print('\n')

temperaturas_cidades = {
    'Jaboticabal': 30,
    'Ribeirão Preto': 35,
    'Montreal': -13,
    'Franca': 33,
    'São Carlos': 28,
    'Botucatu': 27,
    'Toronto': -30
}

for cidade, temperatura in temperaturas_cidades.items():
    if temperatura < 0:
        print(f'A temperatura em {cidade} é negativa, com {temperatura}ºC.')
    else:
        print(f'A temperatura em {cidade} é positiva, com {temperatura}ºC.')
