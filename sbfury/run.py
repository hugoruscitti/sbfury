# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import escena_juego

titulo = "Shaolin's Blind Fury"
#pilas.iniciar_con_asistente(ancho=853, alto=480, titulo=titulo)
pilas.iniciar(ancho=853, alto=480, usar_motor='qtgl', titulo=titulo)

# Cargando la nueva escena.
escena_juego.EscenaJuego()

pilas.ejecutar()
