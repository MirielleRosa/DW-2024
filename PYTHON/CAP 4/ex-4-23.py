from datetime import datetime

data1 = datetime(2022, 1, 1)
data2 = datetime(2022, 2, 1)

diferenca_dias = (data2 - data1).days

print(f"A diferença entre {data1.strftime('%d/%m/%Y')} e {data2.strftime('%d/%m/%Y')} é de {diferenca_dias} dias.")
