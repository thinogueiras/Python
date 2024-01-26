def show_message():
    print('Curso Completo de Python pelo Youtube!!!')


show_message()


def soma(a, b):
    resultado = a + b
    print(resultado)


soma(12, 13)


def mult(x, y):
    return x * y


print(mult(3, 2))


def divisao(k, j):
    if j != 0:
        return k / j
    else:
        return 'Impossível dividir por zero!'


if __name__ == '__main__':
    a = int(input('\nDigite um número: '))
    b = int(input('Digite outro número: '))

    resultado = divisao(a, b)

    print(f'\n{a} dividido por {b} é igual a {resultado}')

print('\n')


def quadrado(num):
    return f'O quadrado do número {num} é {num ** 2}'


lista = [2, 4, 6, 8, 10]

for x in lista:
    print(quadrado(x))

print('\n')


def quadrados(valores):
    quadrados = []
    if isinstance(valores, list):  # É uma instância de lista?
        if all(isinstance(valor, int) for valor in valores):  # Os números da lista são inteiros?
            for x in valores:
                quadrados.append(x ** 2)
            return quadrados
        else:
            return f'A lista deve possuir apenas números inteiros'
    elif isinstance(valores, int):
        return f'\n{valores} elevado ao quadrado é {valores ** 2}'
    else:
        return f'\n{valores} não é um número inteiro!!!'


lista = 'z'
resultado = quadrados(lista)
print(resultado)

print('\n')


def contar(num=11, caractere='*'):
    for i in range(1, num):
        print(caractere)


contar(num=2, caractere='//')
