idade = int(input("Digite sua idade: "))

if idade < 21:
    print("Você é jovem.")
elif 21 <= idade <= 60:
    print("Você é adulto.")
else:
    print("Você é idoso.")
