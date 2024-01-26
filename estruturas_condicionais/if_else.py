#########################################################################
print('\n#########################################################################')

nome = "Thiago"

if nome in ["João", "José", "Antônio"]:
    print("Acesso liberado")
else:
    print("Acesso negado")

#########################################################################
print('\n#########################################################################')

nota1 = nota2 = 0.0
media = 0.0

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('Aluno aprovado com a média:', str(media))
    if media >= 9:
        print('PARABÉNS !!!!')
elif media >= 5:
    print('Aluno está de recuperação', str(media))
else:
    print('Aluno reprovado com a média: {}'.format(media))
    if media < 5.0:
        print('Estude e se esforce mais !!!!')
