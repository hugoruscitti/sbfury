import pilas
import shaolin
import enemigos
import escenario

lista_enemigos = []

pilas.iniciar(ancho=853, alto=480, usar_motor='qtgl', titulo="Shaolin's Blind Fury")

lista_enemigos.append(enemigos.Red())

shaolin.Shaolin(lista_enemigos)
escenario.Escenario()

#pilas.mundo.camara.x = [5300 - 640], 3
#pilas.mundo.camara.x = [100], 40
pilas.ejecutar()
