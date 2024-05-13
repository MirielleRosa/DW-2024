vinhos = [
    {"nome": "Cabernet Sauvignon", "preco": 60},
    {"nome": "Chardonnay", "preco": 45},
    {"nome": "Merlot", "preco": 55},
    {"nome": "Pinot Noir", "preco": 70},
    {"nome": "Sauvignon Blanc", "preco": 40}
]

vinhos_caros = list(filter(lambda vinho: vinho["preco"] > 50, vinhos))
print("Vinhos caros:", vinhos_caros)
