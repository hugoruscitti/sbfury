# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import enemigos

from PyQt4 import QtCore


class Layer(pilas.actores.Actor):
    pass


class Layer3D(Layer):

    def __init__(self, *k):
        Layer.__init__(self, *k)
        self._escala = 0.780
        self._escala_y = 1
        self._angulo = 70
        self._mi_y = 115

    def dibujar(self, painter):
        painter.save()

        transform = painter.transform()
        transform.translate(73, self._mi_y)
        transform.scale(self._escala, self._escala_y)
        transform.rotate(self._angulo, QtCore.Qt.XAxis)
        transform.shear(-0.3, 0)
        painter.setTransform(transform)

        self.imagen.dibujar(painter, self.x, 0, 0, 0, 1, 1, 0, 0)
        painter.restore()


class Escenario:
    """Controla la apariencia del escenario y el desplazamiengo de cámara.

    El escenario se va moviendo a medida que el protagonista avanza, y
    en determinados puntos del escenario construye nuevo enemigos.
    """

    def __init__(self, escena_juego):
        self.bloqueada = False
        fondos = [
                    ("nivel1/layer_3.png", -320, 240, 500),
                    ("nivel1/layer_2.png", -320, 240, 450),
                    ("nivel1/layer_1.png", -320, 240, 440),
                    ("nivel1/layer_0.png", -320,  19, 430),
                 ]
        self.capas = []

        for index, (imagen, x, y, z) in enumerate(fondos):
            if index == 3:
                capa = Layer3D(imagen)
            else:
                capa = Layer(imagen)

            capa.centro = ("izquierda", "arriba")
            capa.x = x
            capa.y = y
            capa.z = z

            self.capas.append(capa)

        self.escena_juego = escena_juego
        self.shaolin = escena_juego.shaolin
        self.cargar_temporizador()
        self._crear_capas()

        self.enemigos = [
            (0, CrearEnemigo(enemigos.Caja, 100, -120)),
            (0, CrearEnemigo(enemigos.Caja, 0, -140)),
            (0, CrearEnemigo(enemigos.Hannia, 500, -140)),
            #(1, PasarDeNivel()),
            (500, CrearEnemigo(enemigos.Red, 500 - 500, -150)),
            (800, CrearEnemigo(enemigos.Red, 880, -200)),
        ]

    def cargar_temporizador(self):
        pilas.mundo.agregar_tarea_siempre(0.1, self.mover_camara)

    def mover_camara(self):

        if not self._esta_bloqueada():
            camara = pilas.escena_actual().camara

            if camara.x + 100 < self.shaolin.x:
                ancho_maximo = self.capas[3].ancho
                ancho_pantalla = 853
                limite = ancho_maximo - ancho_pantalla

                to_x = self.shaolin.x - 100

                if to_x > limite:
                    to_x = limite

                camara.x = [to_x], 0.1

            self._procesar_creacion_de_enemigos(camara.x)

    def _procesar_creacion_de_enemigos(self, camara_x):
        a_eliminar = []

        for x_creacion, item in self.enemigos:
            if camara_x >= x_creacion:
                item.ejecutar(self)
                a_eliminar.append((x_creacion, item))

        if a_eliminar:
            for x in a_eliminar:
                self.enemigos.remove(x)

    def _esta_bloqueada(self):
        """Retorna True si la camara tiene que permanecer estática."""
        if self.bloqueada:
            if self.escena_juego.cantidad_de_enemigos == 0:
                self.bloqueada = False

        return self.bloqueada

    def _crear_capas(self):
        fondo = pilas.fondos.Desplazamiento()
        ancho = 853 # de la pantalla
        maximo_scroll = float(self.capas[3].ancho - ancho)

        fondo.agregar(self.capas[0], (self.capas[0].ancho - ancho) / maximo_scroll)
        fondo.agregar(self.capas[1], (self.capas[1].ancho - ancho) / maximo_scroll)
        fondo.agregar(self.capas[2], 1)
        fondo.agregar(self.capas[3], 1)

    def bloquear_camara(self):
        self.bloqueada = True


class Item:
    """Representa un elemento del escenario que se tiene que construir."""

    def ejecutar(self):
        raise Exception("Metodo no implementado")

class CrearEnemigo(Item):
    """Representa al creación de un enemigo."""

    def __init__(self, clase_enemigo, x, y):
        self.clase_enemigo = clase_enemigo
        self.x = x
        self.y = y

    def ejecutar(self, escenario):
        escenario.escena_juego.crear_enemigo(self.clase_enemigo, self.x, self.y)

class PausaHastaEliminarEnemigos(Item):
    """Realiza una bloqueo del desplazamiento de camara en el escenario.

    Este bloqueo de desplazamiento queda activo hasta que se logren
    eliminar a todos los enemigos que existan en la pantalla."""

    def ejecutar(self, escenario):
        escenario.bloquear_camara()

class PasarDeNivel(Item):
    """Cambia el estado del escenario para indicar que se
    pasa al siguiente nivel."""

    def ejecutar(self, escenario):
        escenario.escena_juego.nivel_terminado()
