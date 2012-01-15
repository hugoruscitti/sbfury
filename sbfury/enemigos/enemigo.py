import pilas


class Enemigo(pilas.actores.Actor):

    def __init__(self):
        self.puede_ser_golpeado = True
        pilas.actores.Actor.__init__(self, "red/parado.png")
