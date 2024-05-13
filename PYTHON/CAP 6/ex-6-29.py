numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = (x ** 2 for x in numeros)

for quadrado in quadrados:
    print(quadrado)
