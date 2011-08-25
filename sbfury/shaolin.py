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
        if pilas.mundo.control.izquierda:
            self.espejado = True

if __name__ == '__main__':
    pilas.iniciar()
    shaolin = Shaolin()
    pilas.ejecutar()
