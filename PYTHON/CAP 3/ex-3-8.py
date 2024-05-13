numero = int(input("Digite um número para calcular seu fatorial: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}.")
