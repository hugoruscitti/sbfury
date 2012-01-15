# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import sombra
import enemigo

class Red(enemigo.Enemigo):

    def __init__(self):
        enemigo.Enemigo.__init__(self)
        self.z = 0
        self.centro = ("centro", "abajo")
        self.x = 200
        self.altura_del_salto = 0
        self.sombra = sombra.Sombra()
        self.actualizar()

    def actualizar(self):
        self.sombra.actualizar_posicion(self.x, self.y, self.altura_del_salto)
