from datetime import datetime

horario1 = datetime(2022, 1, 1, 8, 0)  
horario2 = datetime(2022, 1, 1, 15, 0) 

diferenca_horas = (horario2 - horario1).seconds / 3600

print(f"A diferença entre {horario1.strftime('%H:%M')} e {horario2.strftime('%H:%M')} é de {diferenca_horas} horas.")
