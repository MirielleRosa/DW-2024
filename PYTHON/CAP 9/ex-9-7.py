class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def tipo_triangulo(self):
        try:
            if self.lado1 <= 0 or self.lado2 <= 0 or self.lado3 <= 0:
                raise ValueError("Os lados do triângulo devem ser positivos.")
            if self.lado1 == self.lado2 == self.lado3:
                print("Triângulo equilátero")
            elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
                print("Triângulo isósceles")
            else:
                print("Triângulo escaleno")
        except ValueError as e:
            print("Erro:", e)

triangulo = Triangulo(3, 4, 5)
triangulo.tipo_triangulo()
