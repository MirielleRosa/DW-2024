class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrar_dados(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)