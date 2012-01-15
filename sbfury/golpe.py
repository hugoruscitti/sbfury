# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar
import pilas
from configuracion import DEPURACION
import efecto_golpe
import random

class Golpe(pilas.actores.Actor):
    """Representa un golpe (invisible) que un actor emite a otro."""

    def __init__(self, actor, estado, enemigos, dx, dy):
        pilas.actores.Actor.__init__(self)
        self.imagen = 'colision.png'
        self.z = -200
        self.actor = actor
        self.dx = dx
        self.dy = dy
        self.enemigos = enemigos
        self.actualizar()

    def actualizar(self):
        if self.actor.espejado:
            self.x = self.actor.x - 50 - self.dx
        else:
            self.x = self.actor.x + 50 + self.dx

        self.y = self.actor.y + self.actor.altura_del_salto + self.dy

        enemigo = self.verificar_colisiones()

        if enemigo:
            self.eliminar()

    def verificar_colisiones(self):
        dx = 30
        for enemigo in self.enemigos:
            if enemigo.abajo < self.arriba < enemigo.arriba or enemigo.abajo < self.abajo < enemigo.arriba:

                toque_izquierda = enemigo.izquierda + dx < self.izquierda < enemigo.derecha -dx
                toque_derecha = enemigo.izquierda + dx < self.derecha < enemigo.derecha -dx

                if toque_derecha and toque_derecha:
                    if abs(enemigo.y - self.actor.y) < 15:
                        x = random.randint(-10, 10)
                        y = random.randint(-10, 10)
                        if toque_izquierda:
                            efecto_golpe.EfectoGolpe(self.x - 50 + x, self.y + y)
                        else:
                            efecto_golpe.EfectoGolpe(self.x + 50 + x, self.y + y)

                        return enemigo



    def dibujar(self, aplicacion):
        if DEPURACION:
            pilas.actores.Actor.dibujar(self, aplicacion)

