import pilas

class Shaolin(pilas.actores.Actor):

    def __init__(self):
        self._cargar_imagenes()
        pilas.actores.Actor.__init__(self)
        self.imagen = self.stand
        self.centro = ("centro","abajo")

    def _cargar_imagenes(self):
        self.stand = pilas.imagenes.cargar_grilla("data/shaolin/stand.png", 4)

    def actualizar(self):
        c = pilas.mundo.control
        if c.izquierda:
            self.espejado = True
        elif c.derecha:
            self.espejado = False

if __name__ == '__main__':
    pilas.iniciar()
    shaolin = Shaolin()
    pilas.ejecutar()
