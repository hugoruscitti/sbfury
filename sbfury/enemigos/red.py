# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import sombra
import enemigo
import estados

class Red(enemigo.Enemigo):
    """El Ninja de color rojo"""

    def __init__(self):
        enemigo.Enemigo.__init__(self)
        self._cargar_animaciones()
        self.z = 0
        self.centro = ("centro", "abajo")
        self.x = 200
        self.altura_del_salto = 0
        self.actualizar()
        self.aprender(pilas.habilidades.Arrastrable)
        self.cambiar_animacion('camina')
        self.hacer(estados.Parado())

    def actualizar(self):
        enemigo.Enemigo.actualizar(self)
        self.avanzar_animacion(0.15)

    def _cargar_animaciones(self):
        cargar = pilas.imagenes.cargar_grilla
        self.animaciones = {
                'parado': cargar("red/parado.png", 1),
                'lo_golpean': cargar("red/lo_golpean.png", 1),
                'lo_golpean_fuerte': cargar("red/lo_golpean_fuerte.png", 2),
                'camina': cargar("red/camina.png", 4),
            }
