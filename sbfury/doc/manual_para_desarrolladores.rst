Shaolin's Blind Fury - Manual para desarrolladores
==================================================


Introducción
------------

Este documento es una guia práctica para todos
los desarrolladores que quieran ver o modificar
el código del videojuego ``Shaolin's Blind Fury``.


El documento está separado en varias partes para simplificar
la lectura, pero se intentará mostrar todas las decisiones
de diseño y las estrategias que hacen funcionar al juego.


El protagonista: Shaolin
------------------------

El código del protagonista del juego está en el
directorio ``shaolin``. Gran parte de su funcionalidad
está en dividida en estados.

Para diseñar al shaolin, se usa el patrón de diseño ``state``, en
donde el personaje implementa cada uno de sus movimientos (o
estados) en un objeto, y cada vez que hace algo distinto
simplemente cambia de estado.

Por ejemplo, para hacer que el personaje se quede parado, se
ejecuta esta sentencia:

.. code-block:: python

    shaolin.hacer(estados.Parado()


Este método ``hacer``, toma un objeto comportamiento, y cada
vez que se actualiza al shaolin, se actualiza su comportamiento
también.

De esta forma, queda muy bien definido en qué momento el
personaje ``entra`` en un estado, ``permanece`` en un estado, e
incluso ``cuándo`` sale de un estado.

La codificación del método ``hacer`` está en ``pilas-engine``, pero
se puede ver su código haciendo esto::

    >>> pilas.ver(pilas.actores.Actor.hacer)

Básicamente, un actor tiene una lista de comportamientos, y cuando
llamamos a ``hacer``, ``pilas-engine`` se encarga de tomar el comportamiento
actual y reemplazarlo por otro.

Estados
_______


Los estados del shaolin están en el archivo ``shaolin/estados.py``. Puse a todos
los estados juntos porque tienen mucho en común, casi todos comparten la
misma estructura y son parte del mismo personaje.

Entonces, un estado del personaje es una clase que hereda de los comportamientos
de ``pilas-engine``. Y esta clase tiene una serie de métodos especiales
que permite hacer que el estado interactúe con ``pilas-engine`` y sea parte
de la interacción.

Todo comportamiento tiene que tener un método ``iniciar`` y un método ``actualizar``.

El método ``iniciar`` es invocado por el propio motor ``pilas-engine`` cuando
tiene que llamar al método ``hacer`` sobre un actor. Y el método ``actualizar``
se llama cada vez que se procesa el ``main-loop`` del juego, esto es
exactamente 60 veces por segundo (en ``pilas-engine`` esta frecuencia es fija
en todas las computadoras, lo que puede variar son los fps con que se muestra
(etapa gráfica), pero no la cantidad de veces que es actualizan los actores
(etapa lógica)).


Animaciones
___________


Las animaciones de los personajes están basadas en el código
del actor ``pilas.actores.Cooperativista``, en donde hay solo
tres métodos realmente necesarios para hacer animaciones de un personaje.

Básicamente, las animaciones se guardan en archivos separados, un archivo
por cada animación. Y cada archivo es una grilla en donde están los cuadros
de animación.

Por ejemplo, el archivo ``../data/shaolin/camina.png`` que vemos a continuación:

.. image:: ../data/shaolin/camina.png


tiene todos los cuadros de animación del personaje caminando.

Esta imagen se carga en un diccionario llamado ``animaciones``, dentro
de la clase del shaolin, y luego se controla desde los estados (o comportamientos)
del archivo ``shaolin/estados.py``.

Este es un ejemplo de código reducido de cómo animar un personaje desde
un estado::

    class Caminar(Comportamiento):

        def iniciar(self, shaolin):
            Comportamiento.iniciar(self, shaolin)
            self.shaolin.cambiar_animacion('camina')

        def actualizar(self):
            self.shaolin.avanzar_animacion(0.2)

En el método ``iniciar``, se le dice al shaolin que muestre la animación para
``camina``. Dónde ``camina`` es la clave del diccionario de animaciones, y luego
en ``actualizar`` se pide que avance la animación con una velocidad de ``0.2``, esto
es aproximadamente avanzar 12 cuadros cada un segundo.

Para calcular la velocidad de las animaciones, se puede pensar en la siguiente
cuenta::

    >>> cuandros_a_avanzar_por_segundo = 60 * velocidad

y en este caso daría 12 porque::

    >>> cuandros_a_avanzar_por_segundo = 60 * 0.2
    >>> print cuandros_a_avanzar_por_segundo
    12

Igual, este valor de animación lo calculé probando una y otra vez el
juego ajustando el valor de la velocidad. Comento acá la relación exacta
que tiene con la velocidad real por si te resulta útil para otros juegos.
