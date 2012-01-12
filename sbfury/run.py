import pilas
import shaolin
import enemigos
import escenario

pilas.iniciar(ancho=853, alto=480, usar_motor='qtgl', titulo="Shaolin's Blind Fury")
shaolin.Shaolin()
enemigos.Red()
escenario.Escenario()

#pilas.mundo.camara.x = [5300 - 640], 3
#pilas.mundo.camara.x = [100], 40
pilas.ejecutar()
