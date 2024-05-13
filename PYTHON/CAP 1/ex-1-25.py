nome = input("Digite o nome da pessoa: ")
salario = float(input("Digite o salário da pessoa: "))
imposto = float(input("Digite o valor do imposto: "))

salario_liquido = salario - imposto

print(f"{nome} tem um salário líquido de R$ {salario_liquido:.2f}.")
