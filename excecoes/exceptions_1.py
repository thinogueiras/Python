def div(x, y):
    return round(x / y, 2)


while True:
    try:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        break
    except ValueError:
        print('\nOcorreu um erro ao ler o valor. Tente novamente.\n')
try:
    resultado = div(n1, n2)
except ZeroDivisionError:
    print('\nNão é possível dividir por zero!!!')
except:
    print('\nOcorreu um erro desconhecido')
else:
    print(f'\nResultado: {resultado}')
finally:
    print('\nFim do programa!!!')
