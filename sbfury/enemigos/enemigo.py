# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import personaje

class Enemigo(personaje.Personaje):

    def __init__(self):
        personaje.Personaje.__init__(self)
        self.imagen = "red/parado.png"
        self.velocidad = 2

    def reducir_energia(self, cantidad):
        "Reduce la energia del enemigo y emite evento avisando a la barra de energia."
        self.energia -= cantidad
        pilas.eventos.se_golpea_a_enemigo.emitir(quien=self)
