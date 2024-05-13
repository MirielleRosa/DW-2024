gerador_sequencia_infinita = (x for x in range(1, float('inf')))

print("Os primeiros 10 números da sequência infinita:")
for _ in range(10):
    print(next(gerador_sequencia_infinita))
