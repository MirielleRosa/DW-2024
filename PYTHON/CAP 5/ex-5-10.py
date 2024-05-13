transformarLista = lambda lista, funcao: [funcao(item) for item in lista]

porExtenso = lambda numero: ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"][numero]

numeros = [1, 2, 3, 4, 5]
numeros_extenso = transformarLista(numeros, porExtenso)
print("Números por extenso:", numeros_extenso)
