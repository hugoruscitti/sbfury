# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import time

class Control(pilas.control.Control):

    def __init__(self, escena):
        pilas.control.Control.__init__(self, escena)
        self.historico = [(0, ' ')] * 3
        self.corre = False

    def cuando_pulsa_una_tecla(self, evento):
        self.procesar_cambio_de_estado_en_la_tecla(evento.codigo, True)
        if not evento.es_repeticion:
            self.registrar_tecla(evento.codigo)

    def cuando_suelta_una_tecla(self, evento):
        self.procesar_cambio_de_estado_en_la_tecla(evento.codigo, False)

        if not evento.es_repeticion:
            self.registrar_tecla(" ")

    def registrar_tecla(self, tecla):
        self.historico.append((time.time(), tecla))
        self.historico.pop(0)

        teclas_pulsadas = [tecla for (tiempo, tecla) in self.historico]
        self.corre = False

        # Si ha pulsado para comenzar a correr.
        if teclas_pulsadas == [2, ' ', 2] or teclas_pulsadas == [1, ' ', 1]:
            # Se asegura de que la pulsación ha sido rápida.
            ultimo_time = self.historico[-1][0]
            anteultimo_time = self.historico[-2][0]

            dt = ultimo_time - anteultimo_time

            if dt < 0.15:
                self.corre = True
