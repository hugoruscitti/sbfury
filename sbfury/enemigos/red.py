import pilas

class Red(pilas.actores.Actor):

    def __init__(self):
        pilas.actores.Actor.__init__(self, "red/stand.png")
        self.z = 0
        self.centro = ("centro", "abajo")
