numero = int(input("Digite um número para verificar se é perfeito: "))

soma_divisores = 0

for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i

if soma_divisores == numero:
    print(f"O número {numero} é perfeito.")
else:
    print(f"O número {numero} não é perfeito.")
