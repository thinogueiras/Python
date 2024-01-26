#########################################################################
print('\n#########################################################################')

idade = 34
altura = 1.76

resutado = (idade >= 18) and (altura >= 1.70)
msg = 'Pode participar do evento? ' + str(resutado)

print(msg)

#########################################################################
print('\n#########################################################################')

porta = 'a'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg = 'Alarme acionado? ' + str(alarme)

print(msg)

#########################################################################
print('\n#########################################################################')

tem_dinheiro = True
msg = 'Tem dinheiro? ' + str(tem_dinheiro)

print(msg)

tem_dinheiro = not tem_dinheiro
msg = 'Tem dinheiro? ' + str(tem_dinheiro)

print(msg)
