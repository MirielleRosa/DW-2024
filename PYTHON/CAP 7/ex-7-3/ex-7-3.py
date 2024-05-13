with open("DW-2024/PYTHON/CAP 7/ex-7-3/entrada.txt", "r") as arquivo_entrada:
    linhas = arquivo_entrada.readlines()

linhas = [linha.strip() for linha in linhas]

linhas_invertidas = reversed(linhas)

with open("DW-2024/PYTHON/CAP 7/ex-7-3/saida.txt", "w") as arquivo_saida:
    for linha in linhas_invertidas:
        arquivo_saida.write(linha + '\n')
