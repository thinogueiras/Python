planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao)

astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa de Halley'}

print('\n', astros1 | astros2)
print(astros1.union(astros2))

print('\n', astros1 & astros2)
print(astros1.intersection(astros2))

print('\n', astros1 ^ astros2)
print(astros1.symmetric_difference(astros2))

print('\n')

novos_astros = ['Urano', 'Sol', 'Netuno']
for astro in novos_astros:
    astros1.add(astro)
    print(astros1)
