# Função Type

nome = 'Thiago'
print(type(nome))

media = 0
print(type(media))

n1 = n2 = n4 = n4 = 0.0
print(type(n1))

nome, idade = 'Diego', 47
print(type(nome), type(idade))

status = True
print(type(status))

print(type(1 + 2j))

# Função isinstance()

a = 10
b = 'Sol'

print(isinstance(a, int))
print(isinstance(b, str))

print(isinstance(a, (int, float)), isinstance(b, bool))

# Escopo de variáveis

var_global = 'Curso Completo de Python'


def escreve_texto():
    var_local = 'Python 2024'
    print(f'\nVariável Global: {var_global}')
    print(f'\nVariável Local: {var_local}')


escreve_texto()
