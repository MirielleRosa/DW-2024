gerador_fibonacci = (lambda: (a[0], a.__setitem__(0, a[1]), a.__setitem__(1, a[0] + a[1])) and a[0])([0, 1] * (1 << 64))

print("Os primeiros 20 números da sequência de Fibonacci:")
for _ in range(20):
    print(next(gerador_fibonacci))
