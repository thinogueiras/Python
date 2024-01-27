var1 = 12
var2 = 31

menor = var1 if var1 < var2 else var2

print(f'Menor valor: {menor}')

var1 = 35
var2 = 31

menor = var1 if var1 < var2 else var2

print(f'Menor valor: {menor}')

var1 = 32
var2 = 31

print(f'Menor valor: {(var2, var1)[var1 < var2]}') # Retorna var1 se a expressão for verdadeira
