import os
import zipfile

diretorio = "DW-2024/PYTHON/CAP 7/ex-7-10/"

os.makedirs(os.path.join(diretorio, "Textos"))
for i in range(1, 4):
    with open(os.path.join(diretorio, f"Textos/texto{i}.txt"), "w") as f:
        f.write("Python Essencial")

with zipfile.ZipFile(os.path.join(diretorio, "Textos.zip"), "w") as zipf:
    for root, dirs, files in os.walk(os.path.join(diretorio, "Textos")):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(diretorio, "Textos")))

print("Diretório 'Textos' e seus arquivos foram compactados com sucesso!")
