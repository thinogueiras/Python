from collections import Counter


def numeros_mais_comuns(lista, n=6):
    contagem = Counter(lista)
    numeros_mais_comuns = contagem.most_common(n)

    print(f'\nOs {n} números mais comuns são:')
    for numero, ocorrencias in numeros_mais_comuns:
        print(f'Número: {numero}, Ocorrências: {ocorrencias}')


# Exemplo de uso
lista_numeros = [1, 2, 1, 3, 4, 2, 3, 4, 3, 3, 3, 3, 4, 22, 4, 22,
                 1, 22, 3, 1, 3, 5, 2, 4, 5, 4, 2, 2, 4, 4, 5, 6, 7, 6, 6, 6]
numeros_mais_comuns(lista_numeros, 6)
