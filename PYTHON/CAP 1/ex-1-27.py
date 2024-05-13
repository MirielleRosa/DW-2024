valor_inicial = float(input("Digite o valor inicial do investimento: "))
taxa_juros_mensal = float(input("Digite a taxa de juros mensal (em porcentagem): ")) / 100
meses = int(input("Digite o número de meses que o valor ficou investido: "))

valor_final = valor_inicial * (1 + taxa_juros_mensal) ** meses

print(f"O valor final do investimento é R$ {valor_final:.2f}.")
