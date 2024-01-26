lista_bebidas = []

for i in range(3):
    bebida = input('Digite uma bebida favorita: ')
    while bebida in lista_bebidas:
        bebida = input('Bebida já consta na lista, por favor digite outra: ')
    if bebida == 'Chopp' or bebida == 'chopp':
        print(bebida, 'Pinguin !!!')
    lista_bebidas.append(bebida)

lista_bebidas.sort()

print('\nBebidas em ordem alfabética:')
for bebida in lista_bebidas:
    print(bebida)
