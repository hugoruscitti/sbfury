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

        self._crear_eventos_personalizados()

        self._crear_escenario()

    def _crear_eventos_personalizados(self):
        pilas.eventos.se_golpea_a_enemigo = pilas.eventos.Evento("se_golpea_enemigo")
        pilas.eventos.se_golpea_a_enemigo.conectar(self.actualizar_energia_enemigo)

        pilas.eventos.se_golpea_a_shaolin = pilas.eventos.Evento("se_golpea_shaolin")
        pilas.eventos.se_golpea_a_shaolin.conectar(self.actualizar_energia_shaolin)

        pilas.eventos.se_muere_un_enemigo = pilas.eventos.Evento("se_muere_un_enemigo")
        pilas.eventos.se_muere_un_enemigo.conectar(self._cuando_muere_un_enemigo)

        pilas.eventos.se_muere_el_shaolin = pilas.eventos.Evento("se_muere_el_shaolin")
        pilas.eventos.se_muere_el_shaolin.conectar(self._cuando_muere_el_shaolin)

    def _crear_escenario(self):
        escenario.Escenario(self)

    def crear_enemigo(self, clase, x, y):
        self.lista_enemigos.append(clase(self.shaolin, x=x, y=y))
        self.cantidad_de_enemigos += 1

    def _cuando_muere_un_enemigo(self, evento):
        #actor_que_muere = evento.actor
        self.cantidad_de_enemigos -= 1

    def _cuando_muere_el_shaolin(self, evento):
        #referencia_al_shaolin_que_muere = evento.actor
        texto_game_over = pilas.actores.Texto("Game Over", magnitud=40)
        texto_game_over.z = -1000
        texto_game_over.escala = 0.1
        texto_game_over.escala = [1], 0.5


    def _crear_barras_de_energia(self):
        self.energia_shaolin = pilas.actores.Energia(x=-315, y=213, alto=20)
        self.energia_enemigo = pilas.actores.Energia(x=+315, y=213, alto=20)

    def actualizar_energia_enemigo(self, evento):
        self.energia_enemigo.progreso = evento.quien.energia

    def actualizar_energia_shaolin(self, evento):
        self.energia_shaolin.progreso = evento.quien.energia
