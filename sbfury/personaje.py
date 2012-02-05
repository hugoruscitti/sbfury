# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar
import pilas
import sombra

class Personaje(pilas.actores.Actor):
    """Representa a un actor del videojuego dentro de la escena.

    Esta es la superclase de todos los luchadores, incluido el
    protagonista."""

    def __init__(self):
        pilas.actores.Actor.__init__(self)
        self.sombra = sombra.Sombra()
        self.altura_del_salto = 0
        self.tmp_velocidad_animacion = 0
        self.velocidad = 4

    def actualizar(self):
        pilas.actores.Actor.actualizar(self)
        self.sombra.actualizar_posicion(self.x, self.y, self.altura_del_salto)

    def mover(self, x, y):
        """Hace que el personaje se mueva por el escenario, pero
        prohibiendo movimientos fuera del escenario.
        """
        self.x += x * self.velocidad
        self.y += y * self.velocidad

        # acota 'y' a valores entre -230 y 5
        self.y = min(max(-250, self.y), 5)
        self.z = self.y
        self.x = max(self.x, -400)

    def dibujar(self, applicacion):
        """Redefine la forma de dibujar al actor para que se puede despegar
        del suelo con un salto o ante una caida."""

        if self.altura_del_salto:
            self.y += self.altura_del_salto

        pilas.actores.Actor.dibujar(self, applicacion)

        if self.altura_del_salto:
            self.y -= self.altura_del_salto

    def avanzar_animacion(self, velocidad=1):
        self.tmp_velocidad_animacion += velocidad

        if self.tmp_velocidad_animacion > 1:
            self.tmp_velocidad_animacion -= 1
            return self.imagen.avanzar()

    def definir_cuadro(self, indice):
        self.imagen.definir_cuadro(indice)                                                       
        self.tmp_velocidad_animacion = 0

    def cambiar_animacion(self, nombre):
        self.imagen = self.animaciones[nombre]
        self.centro = ("centro", "abajo")

    def _cargar_animaciones(self):
        #cargar = pilas.imagenes.cargar_grilla
        self.animaciones = {
                # 'animacion': cargar("archivo.png", 3),
            }
