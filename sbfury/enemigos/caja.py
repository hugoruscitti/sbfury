# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import enemigo
import estados
import red

class Caja(red.Red):

    def _iniciar(self):
        self.miniatura = pilas.imagenes.cargar("objetos/caja_mini.png")
        self.hacer(estados.CajaEnReposo())

    def _cargar_animaciones(self):
        cargar = pilas.imagenes.cargar_grilla
        self.imagen = cargar("objetos/caja.png", 2)

    def actualizar(self):
        self.sombra.actualizar_posicion(self.x, self.y, 100)


class CajaParte(pilas.actores.Actor):

    def __init__(self, imagen, x, y, dx, dy):
        pilas.actores.Actor.__init__(self, imagen, x, y)
        self.x = [self.x + dx], 1
        self.transparencia = [100], 1
        self.contandor = 0
        self.dy = dy
        self.y_inicial = y
        self.puede_ser_golpeado = False
        self.centro = ("centro", "abajo")

        if dx < 0:
            self.espejado = True
    
    def actualizar(self):
        self.contandor += 1
        self.dy -= 0.20
        self.y += self.dy

        if self.y < self.y_inicial:
            self.dy *= -1
            self.dy /= 2

        if self.contandor > 80:
            self.eliminar()
