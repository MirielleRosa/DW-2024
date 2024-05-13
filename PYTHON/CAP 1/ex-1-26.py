import math

altura_inicial = float(input("Digite a altura inicial do objeto em metros: "))
gravidade = 9.8  

tempo = math.sqrt((2 * altura_inicial) / gravidade)

print(f"O objeto leva {tempo:.2f} segundos para atingir o solo.")
