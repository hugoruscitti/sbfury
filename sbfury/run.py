# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import escena_juego

pilas.iniciar(ancho=853, alto=480, usar_motor='qtgl', titulo="Shaolin's Blind Fury")

# Cargando la nueva escena.
escena_juego.EscenaJuego()

pilas.ejecutar()
