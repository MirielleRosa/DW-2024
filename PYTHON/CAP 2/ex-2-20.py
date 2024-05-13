cpf = input("Digite o número de CPF (apenas números): ")

if len(cpf) == 11 and cpf.isdigit():
    print("CPF válido.")
else:
    print("CPF inválido.")
