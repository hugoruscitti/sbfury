# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import enemigo
import estados
import red

class Hannia(red.Red):

    def _iniciar(self):
        # inicia la lista de comportamientos para inteligencia artificia (AI)
        self.comportamientos_ai = [
                    estados.Parado(segundos=1),
                    estados.CaminarAleatoriamente(segundos=0.5),
                    estados.Parado(segundos=1),
                    estados.CaminaHaciaLineaVerticalDelShaolin(segundos=1),
                    ]
        self.comportamiento_ai_indice = 0
        self.hacer(estados.IngresarCayendo())

    def _cargar_animaciones(self):
        cargar = pilas.imagenes.cargar_grilla
        self.animaciones = {
                'parado': cargar("hannia/parado.png", 1),
                #'golpear': cargar("red/golpear.png", 3),
                'lo_golpean': cargar("hannia/lo_golpean.png", 1),
                'lo_golpean_fuerte': cargar("hannia/lo_golpean_fuerte.png", 2),
                'caminar': cargar("hannia/caminar.png", 4),
                #'lanzar': cargar("red/lanzar.png", 4),
                'saltando': cargar("hannia/saltando.png", 1),
            }
