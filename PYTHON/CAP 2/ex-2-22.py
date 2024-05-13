clima = input("Digite a descrição do clima (ensolarado, chuvoso, nublado, etc.): ")

match clima.lower():
    case "ensolarado":
        print("Sugestão: Óculos de sol e roupas leves.")
    case "chuvoso":
        print("Sugestão: Guarda-chuva e casaco impermeável.")
    case "nublado":
        print("Sugestão: Casaco leve e guarda-chuva (se necessário).")
    case "frio":
        print("Sugestão: Casaco quente, cachecol e luvas.")
    case _:
        print("Não temos uma sugestão específica para este clima.")
