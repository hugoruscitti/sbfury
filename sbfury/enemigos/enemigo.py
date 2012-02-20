# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import personaje

class Enemigo(personaje.Personaje):

    def __init__(self):
        self.puede_ser_golpeado = True
        personaje.Personaje.__init__(self)
        self.imagen = "red/parado.png"
        self.velocidad = 2

    def ha_sido_golpeado(self, quien, fuerte=False):
        self.comportamiento_actual.ha_sido_golpeado(quien, fuerte)

    def reducir_energia(self, cantidad):
        "Reduce la energia del enemigo y emite evento avisando a la barra de energia."
        self.energia -= cantidad
        pilas.eventos.se_golpea_a_enemigo.emitir(quien=self)

