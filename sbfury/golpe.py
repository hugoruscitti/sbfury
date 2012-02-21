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

    def __init__(self, actor, enemigos, dx, dy):
        pilas.actores.Actor.__init__(self)
        self.imagen = 'colision.png'
        self.actor = actor
        self.dx = dx
        self.dy = dy
        self.enemigos = enemigos
        self.actualizar()

    def actualizar(self):
        if self.actor.espejado:
            self.x = self.actor.x - 70 - self.dx
        else:
            self.x = self.actor.x + 70 + self.dx

        self.y = self.actor.y + self.actor.altura_del_salto + self.dy

    def verificar_colisiones(self):
        for enemigo in self.enemigos:

            area = [
                    enemigo.izquierda + 10, 
                    enemigo.derecha - 10, 
                    enemigo.abajo, 
                    enemigo.arriba,
                   ]

            if enemigo.puede_ser_golpeado:
                # colisión horizontal y vertical de caja contra punto.
                if area[0] < self.x < area[1] and area[2] < self.y < area[3]:      
                    # verificando que están casi en el mismo plano z.
                    if abs(enemigo.y - self.actor.y) < 15:
                        self.crear_efecto_de_golpe()
                        return enemigo

    def dibujar(self, aplicacion):
        if DEPURACION:
            pilas.actores.Actor.dibujar(self, aplicacion)

    def crear_efecto_de_golpe(self):
        dx = random.randint(-10, 10)
        dy = random.randint(-10, 10)
        efecto_golpe.EfectoGolpe(self.x + dx, self.y + dy)
