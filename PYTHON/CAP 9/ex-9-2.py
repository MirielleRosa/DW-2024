def media_aritmetica(lista):
    try:
        if not lista:
            raise ValueError("A lista está vazia.")
        numeros = [float(x) for x in lista]
        return sum(numeros) / len(numeros)
    except ValueError as e:
        return str(e)

numeros = input("Digite os números separados por espaço: ").split()
print(media_aritmetica(numeros))
