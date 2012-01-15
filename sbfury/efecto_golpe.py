# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar
import pilas
import random

class EfectoGolpe(pilas.actores.Animacion):
    """Muestra un destello para representar una colisión de golpe."""

    def __init__(self, x, y):
        grillas = [
                pilas.imagenes.cargar_grilla("golpe_1.png", 2),
                pilas.imagenes.cargar_grilla("golpe_2.png", 2),
            ]
        sonidos = [
            pilas.sonidos.cargar("sonidos/golpe_1.wav"),
            pilas.sonidos.cargar("sonidos/golpe_2.wav"),
            pilas.sonidos.cargar("sonidos/golpe_3.wav"),
            ]

        grilla = random.choice(grillas)
        sonido = random.choice(sonidos)
        sonido.reproducir()
        pilas.actores.Animacion.__init__(self, grilla, ciclica=False, 
            velocidad=10, x=x, y=y)
        self.escala = 0.5
        self.escala = [1.5], 0.1
        self.rotacion = random.choice([0, 45, 90, 150])

