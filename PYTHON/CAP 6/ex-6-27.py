def gerador_fibonacci():
    a = [0, 1]
    while True:
        yield a[0]
        a[0], a[1] = a[1], a[0] + a[1]

fibonacci = gerador_fibonacci()

print("Os primeiros 20 números da sequência de Fibonacci:")
for _ in range(20):
    print(next(fibonacci))
