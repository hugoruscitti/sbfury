# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import enemigo

class Estrella(enemigo.Enemigo):
    """Una estrella ninja que vuela intentando golpear al shaolin."""

    def __init__(self, x, y, direccion, shaolin):
        enemigo.Enemigo.__init__(self)
        self.imagen = "estrella.png"
        self.shaolin = shaolin
        self.centro = ("centro", "centro")
        self.x = x
        self.y = y
        self.altura_del_salto = 100
        self.direccion = direccion
        self.actualizar()
        self.aprender(pilas.habilidades.Arrastrable)

    def actualizar(self):
        enemigo.Enemigo.actualizar(self)
        self.x += self.direccion * 6
        self.rotacion += 10
        self.z = self.y

        # TODO: eliminar si está fuera de la pantalla.
