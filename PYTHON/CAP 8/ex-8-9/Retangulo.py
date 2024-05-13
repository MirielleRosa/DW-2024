class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura

class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

quadrado = Quadrado(5)
print("Área do quadrado:", quadrado.area())
