import pilas
import shaolin
import enemigos
import escenario

pilas.iniciar(usar_motor='qtgl', titulo="Shaolin's Blind Fury")
shaolin.Shaolin()
enemigos.Red()
escenario.Escenario()

pilas.ejecutar()
