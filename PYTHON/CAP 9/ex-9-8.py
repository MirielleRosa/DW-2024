import string

def jogo_adivinhacao_palavra():
    palavra_secreta = "python" 
    tentativas = 3
    
    while tentativas > 0:
        try:
            palpite = input("Adivinhe a palavra secreta: ").lower()
            if all(letra in string.ascii_lowercase for letra in palpite):
                if palpite == palavra_secreta:
                    print("Parabéns! Você acertou!")
                    break
                else:
                    print("Palavra incorreta! Tente novamente.")
                    tentativas -= 1
                    print(f"Tentativas restantes: {tentativas}")
            else:
                raise ValueError("Por favor, insira apenas letras do alfabeto.")
        except ValueError as e:
            print(e)

jogo_adivinhacao_palavra()
