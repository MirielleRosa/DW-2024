jogadores = {}

while True:
    numero_camisa = input("Digite o número da camisa (-1 para sair): ")
    if numero_camisa == "-1":
        break
    nome_jogador = input("Digite o nome do jogador: ")
    jogadores[int(numero_camisa)] = nome_jogador

print("Jogadores ordenados pelo número da camisa:")
for numero_camisa, nome_jogador in sorted(jogadores.items()):
    print(f"Número da camisa: {numero_camisa}, Nome do jogador: {nome_jogador}")
