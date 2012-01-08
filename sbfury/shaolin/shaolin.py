import pilas
import estados

class Shaolin(pilas.actores.Actor):

    def __init__(self):
        self._cargar_animaciones()
        pilas.actores.Actor.__init__(self)
        self.hacer(estados.Parado())
        self.tmp_velocidad_animacion = 0

    def _cargar_animaciones(self):
        cargar = pilas.imagenes.cargar_grilla
        self.animaciones = {
            "parado": cargar("shaolin/parado.png", 4),
            "camina": cargar("shaolin/camina.png", 4),
            "ataca1": cargar("shaolin/ataca1.png", 2),
            "ataca2": cargar("shaolin/ataca2.png", 2),
            "ataca3": cargar("shaolin/ataca3.png", 2),
            "ataca4": cargar("shaolin/ataca4.png", 2),
        }

    def mover(self, x, y):
        """Hace que el personaje se mueva por el escenario, pero
        prohibiendo movimientos fuera del escenario.

            >>> s = Shaolin()
            >>> s.x
            0
            >>> s.mover(10, 0)
            >>> s.x
            10
        """
        self.x += x * 3
        self.y += y * 3

        # acota 'y' a valores entre -230 y 5
        self.y = min(max(-250, self.y), 5)
        self.z = self.y

    def definir_cuadro(self, indice):
        self.imagen.definir_cuadro(indice)                                                       
        self.tmp_velocidad_animacion = 0

    def cambiar_animacion(self, nombre):
        self.imagen = self.animaciones[nombre]
        self.centro = ("centro", "abajo")

    def avanzar_animacion(self, velocidad=1):
        self.tmp_velocidad_animacion += velocidad

        if self.tmp_velocidad_animacion > 1:
            self.tmp_velocidad_animacion -= 1
            return self.imagen.avanzar()
