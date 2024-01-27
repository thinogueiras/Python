valores = [1, 2, 3, 4, 5, 6]

quadrados = (item ** 2 for item in valores)
print(quadrados)

for i in quadrados:
    print(i, end=' ')
