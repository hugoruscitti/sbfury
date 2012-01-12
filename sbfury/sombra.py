import pilas

class Sombra(pilas.actores.Actor):

    def __init__(self):
        pilas.actores.Actor.__init__(self, "sombra.png")
        self.centro = ("centro", "abajo")

    def actualizar_posicion(self, x, y, altura):
        self.x, self.y = x, y
        self.escala = -0.003 * altura + 1
