import pilas
import estados

class Shaolin(pilas.actores.Actor):

    def __init__(self):
        self._cargar_animaciones()
        pilas.actores.Actor.__init__(self)
        self.hacer(estados.Parado())

    def _cargar_animaciones(self):
        cargar = pilas.imagenes.cargar_grilla
        self.animaciones = {
            "stand": cargar("shaolin/stand.png", 4),
            "attack1": cargar("shaolin/attack1.png", 2),
        }

    def mover(self, x, y):
        self.x += x * 3
        self.y += y * 3

        # acota 'y' a valores entre -230 y 100
        self.y = min(max(-230, self.y), 100) 
        self.z = self.y

    def definir_cuadro(self, indice):
        self.imagen.definir_cuadro(indice)                                                       

    def cambiar_animacion(self, nombre):
        self.imagen = self.animaciones[nombre]
        self.centro = ("centro", "abajo")
