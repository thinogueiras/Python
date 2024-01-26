from math import sqrt

if __name__ == '__main__':
    while True:
        try:
            num = int(input('\nDigite um número inteiro positivo: '))
            if num < 0:
                raise ArithmeticError
        except ArithmeticError:
            print('\nFoi fornecido um número negativo!!!')
        else:
            print(f'\nA raíz quadrado de {num} é {round(sqrt(num))}.')
            break
