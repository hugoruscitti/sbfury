import pilas
from configuracion import DEPURACION

class Golpe(pilas.actores.Actor):
    """Representa un golpe (invisible) que un actor emite a otro."""

    def __init__(self, actor, dx, dy):
        pilas.actores.Actor.__init__(self)
        self.imagen = 'colision.png'
        self.contador = 0
        self.z = -200
        self.actor = actor
        self.dx = dx
        self.dy = dy
        self.actualizar()

    def actualizar(self):
        if self.contador > 10:
            self.eliminar()
        else:
            self.contador += 1

        if self.actor.espejado:
            self.x = self.actor.x - 50 - self.dx
        else:
            self.x = self.actor.x + 50 + self.dx

        self.y = self.actor.y + self.actor.altura_del_salto + self.dy

    def dibujar(self, aplicacion):
        if DEPURACION:
            pilas.actores.Actor.dibujar(self, aplicacion)
