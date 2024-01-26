def fatorial(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)


if __name__ == '__main__':
    while True:
        x = int(input('Digite um número inteiro e positivo: '))
        try:
            resultado = fatorial(x)
        except RecursionError:
            print('\nO número é muito grande ou negativo. Tente novamente!!!\n')
        else:
            print(f'\nO fatorial do número {x} é: {resultado}')
            break
