from datetime import datetime, timedelta

hora_atual = datetime.now()

hora_passada = hora_atual - timedelta(hours=2)

print("Hora atual:", hora_atual.strftime('%H:%M:%S'))
print("Hora há 2 horas:", hora_passada.strftime('%H:%M:%S'))
