decifrar_mensagem = lambda mensagem_codificada: "" if not mensagem_codificada else \
    (chr(ord(mensagem_codificada[0]) + 1) if mensagem_codificada[0] != 'z' else 'a') + \
    decifrar_mensagem(mensagem_codificada[1:])

mensagem_codificada = "dbufojt"
mensagem_decifrada = decifrar_mensagem(mensagem_codificada)
print("Mensagem decifrada:", mensagem_decifrada)
