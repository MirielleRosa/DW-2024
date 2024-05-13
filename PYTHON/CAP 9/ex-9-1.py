def divisao():
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    except ValueError:
        print("Por favor, insira apenas números inteiros.")
    except ZeroDivisionError:
        print("Erro: divisão por zero.")

divisao()
