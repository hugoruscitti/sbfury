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
        self.historico = [' '] * 3
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
        self.historico.append(tecla)
        self.historico.pop(0)
        self.corre = (self.historico == [2, ' ', 2] or self.historico == [1, ' ', 1])
