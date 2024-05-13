from Livro import Livro

class LivroDeBiblioteca(Livro):
    def __init__(self, titulo, autor, codigo):
        super().__init__(titulo, autor)
        self.codigo = codigo
    
    def mostrar_dados(self):
        super().mostrar_dados()
        print("Código:", self.codigo)

livro_biblioteca = LivroDeBiblioteca("Dom Quixote", "Mirielle Rosa", "1234567")
livro_biblioteca.mostrar_dados()