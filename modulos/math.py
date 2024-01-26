import math

# Raíz quadrada
print('\nA raíz quadrada de 81 é:', math.sqrt(81).__trunc__())
print('\nA raíz quadrada de 144 é:', math.sqrt(144).__trunc__())

# Potência utilizando a função Pow Builtin
print('\nTrês elevado a terceira potência é:', pow(3, 3).__trunc__())
print('\nTrês elevado a quarta potência é:', pow(3, 4).__trunc__())

# Fatorial
print('\nO fatorial do número 8 é:', math.factorial(8))
print('\nO fatorial do número 3 é:', math.factorial(3))

x = 8

raiz_quadrada = math.sqrt(x)
print(round(raiz_quadrada, 2))
print(f'\n{raiz_quadrada}')
print(math.floor(raiz_quadrada))
print(math.ceil(raiz_quadrada))

y = -25
print('\nA raíz quadrada de -25 é:', round(math.sqrt(abs(y))))

print('\nLog de 100 na base 10 é:', round(math.log10(100)))

print('\nPI:', round(math.pi, 4))
