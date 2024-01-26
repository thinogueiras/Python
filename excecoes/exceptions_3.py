from math import sqrt


class NumeroNegativoError(Exception):
    def __init__(self):
        print('\nFoi fornecido um número negativo!!!')


if __name__ == '__main__':
    while True:
        try:
            num = int(input('\nDigite um número inteiro positivo: '))
            if num < 0:
                raise NumeroNegativoError
        except:
            NumeroNegativoError
        else:
            print(f'\nA raíz quadrado de {num} é {round(sqrt(num))}.')
            break
