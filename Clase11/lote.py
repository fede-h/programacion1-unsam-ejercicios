
class Lote:
    
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = int(cajones)
        self.precio = float(precio)

    def __repr__(self):
        print(f'Lote({self.nombre}, {self.cajones}, {self.precio})')

    def costo(self):
        return (self.cajones * self.precio)

    def vender(self, n):
        self.cajones -= n
