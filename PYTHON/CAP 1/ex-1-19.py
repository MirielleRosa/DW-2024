import math

a = float(input("Digite o comprimento do primeiro cateto: "))
b = float(input("Digite o comprimento do segundo cateto: "))

c = math.sqrt(a**2 + b**2)

print(f"O comprimento da hipotenusa é: {c:.2f}")
