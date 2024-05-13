from datetime import datetime

instante_atual = datetime.now()
instante_futuro = datetime(2025, 1, 1)

if instante_atual < instante_futuro:
    print("O instante atual é anterior ao instante futuro.")
else:
    print("O instante atual é posterior ao instante futuro.")
