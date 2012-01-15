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

    def ha_sido_golpeado(self, otro_actor):
        pass


class Parado(Comportamiento):

    def iniciar(self, enemigo):
        Comportamiento.iniciar(self, enemigo)
        self.enemigo.cambiar_animacion('parado')

    def actualizar(self):
        pass
        
    def ha_sido_golpeado(self, otro_actor):
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
        
    def ha_sido_golpeado(self, otro_actor):
        pass
