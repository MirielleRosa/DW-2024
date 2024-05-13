from Animal import Animal

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au")

cachorro = Cachorro("Rex")
cachorro.emitir_som()