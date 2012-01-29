# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar
import pilas
import random

class Comportamiento(pilas.comportamientos.Comportamiento):

    def iniciar(self, enemigo):
        self.enemigo = enemigo
        self.control = pilas.mundo.control
        self.golpe = None

    #def golpear(self, dx=0, dy=40):
    #    self.golpe = golpe.Golpe(self.shaolin, self, self.shaolin.enemigos, dx, dy)

    #def eliminar_golpe(self):
    #    if self.golpe:
    #        self.golpe.eliminar()
    #        self.golpe = None

    def ha_golpeado(self, otro_actor):
        pass

    def ha_sido_golpeado(self, otro_actor, fuerte=False):
        pass


class Parado(Comportamiento):

    def iniciar(self, enemigo):
        Comportamiento.iniciar(self, enemigo)
        self.enemigo.cambiar_animacion('parado')

    def actualizar(self):
        pass
        
    def ha_sido_golpeado(self, otro_actor, fuerte=False):
        # Mira hacia el lado en donde recibe el golpe.
        self.enemigo.espejado = otro_actor.x < self.enemigo.x

        if fuerte:
            self.enemigo.hacer(LoGolpeanFuerte())
        else:
            self.enemigo.hacer(LoGolpean())


class LoGolpean(Comportamiento):

    def iniciar(self, enemigo):
        Comportamiento.iniciar(self, enemigo)
        self.enemigo.cambiar_animacion('lo_golpean')
        self.x_inicial = self.enemigo.x
        self.y_inicial = self.enemigo.y
        self.contador = 20

    def actualizar(self):
        x = self.x_inicial
        y = self.y_inicial

        self.enemigo.x = random.choice([x - 1, x, x + 1])
        self.enemigo.y = random.choice([y - 1, y, y + 1])

        # timeout para regresar al estado parado:
        if self.contador < 0:
            self.enemigo.x = self.x_inicial
            self.enemigo.y = self.y_inicial
            self.enemigo.hacer(Parado())
        else:
            self.contador -= 1
        
    def ha_sido_golpeado(self, otro_actor, fuerte=False):
        pass

class LoGolpeanFuerte(LoGolpean):

    def iniciar(self, enemigo):
        LoGolpean.iniciar(self, enemigo)
        self.enemigo.puede_ser_golpeado = False
        self.enemigo.cambiar_animacion('lo_golpean_fuerte')
        self.velocidad_general = 14
        self.velocidad_inicial = self.velocidad_general

        if self.enemigo.espejado:
            self.velocidad_horizontal = 1.25
        else:
            self.velocidad_horizontal = -1.25

    def actualizar(self):
        self.enemigo.altura_del_salto += self.velocidad_inicial
        self.velocidad_inicial -= 0.75

        if self.enemigo.altura_del_salto < 30:
            # Si está cerca del suelo se muestra acostado.
            self.enemigo.definir_cuadro(1)
        else:
            self.enemigo.definir_cuadro(0)

        if self.enemigo.altura_del_salto < 0:
            # Si toca el suelo rebota con menos intensidad.
            self.velocidad_horizontal /= 1.5
            self.velocidad_general -= 4
            self.velocidad_inicial = self.velocidad_general
            self.altura_del_salto = 0

            if self.velocidad_general < 0:
                self.terminar_caida()

        self.enemigo.mover(self.velocidad_horizontal, 0)

    def terminar_caida(self):
        self.enemigo.hacer(QuedarseEnElSuelo())


class QuedarseEnElSuelo(Comportamiento):

    def iniciar(self, enemigo):
        Comportamiento.iniciar(self, enemigo)
        self.enemigo.cambiar_animacion('lo_golpean_fuerte')
        self.enemigo.definir_cuadro(1)
        self.contador = 60
        self.enemigo.puede_ser_golpeado = False

    def actualizar(self):
        self.enemigo.definir_cuadro(1)
        self.contador -= 1

        if self.contador < 0:
            self.levantarse()

    def levantarse(self):
        self.enemigo.puede_ser_golpeado = True
        self.enemigo.hacer(Parado())
