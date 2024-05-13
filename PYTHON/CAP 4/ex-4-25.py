from datetime import datetime, timedelta

data_atual = datetime.now()

data_futura = data_atual + timedelta(days=30)

print("Data atual:", data_atual.strftime('%d/%m/%Y'))
print("Data daqui a 30 dias:", data_futura.strftime('%d/%m/%Y'))
