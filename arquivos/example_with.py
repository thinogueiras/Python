caminho = "C:\\Users\\Thiago\\Python\\arquivos"

try:
    arquivo = open(caminho + "\\" + "frutas.txt", 'r', encoding='utf-8')
    print(arquivo.read())
except IOError:
    print(f'\nNão foi possível abrir o arquivo')
else:
    arquivo.close()


with open(caminho + "\\" + "frutas.txt", 'r', encoding='utf-8') as frutas:
    for fruta in frutas:
        print(fruta)
