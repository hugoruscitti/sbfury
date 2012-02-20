# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import shaolin
import escenario

from pilas.escenas import Normal


class EscenaJuego(Normal):
    """Representa la escena de juego en donde el shaolin va luchando."""

    def __init__(self):
        Normal.__init__(self)
        self.lista_enemigos = []
        self.cantidad_de_enemigos = 0

        self._crear_barras_de_energia()

        self.shaolin = shaolin.Shaolin(self.lista_enemigos)

        pilas.eventos.se_muere_un_enemigo = pilas.eventos.Evento("se_golpea_enemigo")
        pilas.eventos.se_muere_un_enemigo.conectar(self._cuando_mueve_un_enemigo)

        self._crear_escenario()

    def _crear_escenario(self):
        escenario.Escenario(self)

    def crear_enemigo(self, clase, x, y):
        self.lista_enemigos.append(clase(self.shaolin, x=x, y=y))
        self.cantidad_de_enemigos += 1

    def _cuando_mueve_un_enemigo(self, evento):
        #actor_que_muere = evento.actor
        self.cantidad_de_enemigos -= 1

    def _crear_barras_de_energia(self):
        self.energia_shaolin = pilas.actores.Energia(x=-315, y=213, alto=20)
        self.energia_enemigo = pilas.actores.Energia(x=+315, y=213, alto=20)

        pilas.eventos.se_golpea_a_enemigo = pilas.eventos.Evento("se_golpea_enemigo")
        pilas.eventos.se_golpea_a_enemigo.conectar(self.actualizar_energia_enemigo)

    def actualizar_energia_enemigo(self, evento):
        self.energia_enemigo.progreso = evento.quien.energia
