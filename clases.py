class Rectangulo:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def area(self):
        return self.ancho * self.altura

    def __str__(self):
        return f"Rectángulo de {self.ancho} por {self.altura}"

    def __eq__(self, otro):
        return self.ancho == otro.ancho and self.altura == otro.altura


                        