import os

diretorio = "DW-2024/PYTHON/CAP 7/ex-7-6/"

nome_arquivo_origem = input("Digite o nome do arquivo a ser copiado: ")
caminho_arquivo_origem = os.path.join(diretorio, nome_arquivo_origem)

nome_arquivo_destino = nome_arquivo_origem.split('.')[0] + ".cópia"
caminho_arquivo_destino = os.path.join(diretorio, nome_arquivo_destino)

with open(caminho_arquivo_origem, 'r') as origem:
    with open(caminho_arquivo_destino, 'w') as destino:
        destino.write(origem.read())

print(f"Arquivo {caminho_arquivo_origem} copiado para {caminho_arquivo_destino} com sucesso!")