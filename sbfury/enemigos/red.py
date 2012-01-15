# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import sombra

class Red(pilas.actores.Actor):

    def __init__(self):
        pilas.actores.Actor.__init__(self, "red/stand.png")
        self.z = 0
        self.centro = ("centro", "abajo")
        self.x = 200
        self.altura_del_salto = 0
        self.sombra = sombra.Sombra()
        self.actualizar()

    def actualizar(self):
        self.sombra.actualizar_posicion(self.x, self.y, self.altura_del_salto)
