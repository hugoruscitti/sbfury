# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import shaolin
import enemigos
import escenario

from pilas.escenas import Normal

class EscenaJuego(Normal):

    def __init__(self):
        print "comenzando la escena de juego..."
        self.lista_enemigos = []
        s = shaolin.Shaolin(self.lista_enemigos)
        self._crear_eventos_personalizados()
        self.lista_enemigos.append(enemigos.Red(s))
        escenario.Escenario(s)

        self._crear_barras_de_energia()

    def _crear_barras_de_energia(self):
        energia_shaolin = pilas.actores.Energia(x=-315, y=213, alto=20)
        energia_enemigo = pilas.actores.Energia(x=310, y=213, alto=20)
        energia_enemigo.progreso = 100 

        def actualizar_energia_enemigo(evento):
            energia_enemigo.progreso = evento.quien.energia

        pilas.eventos.se_golpea_a_enemigo.conectar(actualizar_energia_enemigo)

    def _crear_eventos_personalizados(self):
        pilas.eventos.se_golpea_a_enemigo = pilas.eventos.Evento(['quien', 'energia'])




