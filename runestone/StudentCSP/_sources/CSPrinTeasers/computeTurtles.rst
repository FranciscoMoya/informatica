..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

..  shortname:: Capítulo: Lo que puedes hacer con un computador
..  description:: Algunas pildoritas de lo que puedes hacer con un computador

.. setup for automatic question numbering.

.. 	qnum::
	:start: 1
	:prefix: csp-1-5-


.. |runbutton| image:: Figures/run-button.png
    :height: 20px
    :align: top
    :alt: run button

.. |audiobutton| image:: Figures/start-audio-tour.png
    :height: 20px
    :align: top
    :alt: audio tour button



Computar con tortugas
=====================

Aquí una tortuga no es un animal.
Trabajamos con una tortuga virtual, una idea que se remonta a los años 1960.  La tortuga robot original sujetaba un rotulador físico.  Los programadores estudiantes dirigían al robot usando programas, y creando dibujos con el rotulador.

.. figure:: Figures/mindstorms_turtle.jpg
    :width: 200px
    :align: center
    :alt: Niños jugando con un robot tortuga Logo que podía dibujar con un rotulador
    :figclass: align-center

    Figura 3: Niños jugando con un robot tortuga Logo que podía dibujar con un rotulador

..	index::
	single: comment
	single: library
	single: screen
	single: comentario
	single: biblioteca
	single: pantalla
	pair: turtle; screen
	pair: turtle; library
	pair: programming; comment
	pair: program; comment
	pair: tortuga; pantalla
	pair: tortuga; biblioteca
	pair: programación; comentario
	pair: programa; comentario

Hoy podemos jugar con tortugas virtuales de una forma completamente gráfica y sin robótica.  A continuación hay un programa Python que primero carga una **biblioteca** que contiene el código que nos permite trabajar con tortugas (``from turtle import *``). Después crea una **Pantalla**, un espacio en la página para que la tortuga se mueva y dibuje (``espacio = Screen()``).  A continuación crea una tortuga llamada ``alex`` (``alex = Turtle()``), después hace que ``alex`` se mueva en la pantalla (``alex.forward(150)``) y cuando se mueve dibuja el camino por donde va.  La parte de cualquier línea que empieza por un carácter ``#`` se llama **comentario**.  Python y el ordenador ignora todo lo que hay desde el carácter ``#`` hasta el final de la línea.   Los **comentarios** explican qué estamos haciendo en el programa y están destinados a ser leídos por personas, no por computadores.

Prueba a pulsar sobre el botón |runbutton| para ver qué hace el siguiente programa.

.. activecode:: Turtle_1
    :tour_1: "Line-by-line Tour"; 1: first-turtle-line-1; 2: first-turtle-line-2; 3: first-turtle-line-3; 4: first-turtle-line-4; 5: first-turtle-line-5; 6: first-turtle-line-6;
    :nocodelens:

    from turtle import *	# usa la biblioteca turtle
    espacio = Screen()		# crea un espacio de tortugas
    alex = Turtle()   		# crea una tortuga llamada alex
    alex.forward(150)		# mueve alex hacia delante 150 unidades
    alex.left(90)   		# gira 90 grados
    alex.forward(75)		# mueve alex hacia delante 75 unidades


..	index::
	single: dot notation
	single: notación punto

.. Note::
   Fíjate en que en el código decimos a ``alex`` qué hacer empleando la **notación punto**: ``alex.forward(150)``, ``alex.left(90)``, y ``alex.forward(75)``.  Esa es la forma en la que te comunicas con la tortuga.  Usas el nombre de la tortuga seguido por un ``.`` y después qué quieres que haga.

.. mchoice:: 1_5_1_Turtle_Q1
   :answer_a: Norte
   :answer_b: Oeste
   :answer_c: Sur
   :answer_d: Este
   :correct: d
   :feedback_a: Comprueba en qué dirección se movió alex al principio
   :feedback_b: Comprueba en qué dirección se movió alex al principio
   :feedback_c: Comprueba en qué dirección se movió alex al principio
   :feedback_d: Las tortugas empiezan orientadas al este por defecto

   ¿En qué dirección se moverá alex cuando se ejecute el código a continuación?

   ::

      from turtle import *
      espacio = Screen()
      alex = Turtle()
      alex.forward(100)

Simplemente yendo hacia delante, detrás, izquierda y derecha, podemos hacer que la tortuga dibuje una figura.

.. fillintheblank:: 1_5_2_Shape_fill

    .. blank:: 1_5_2_Shape
        :correct: ^cuadrado$|^Cuadrado$|^CUADRADO$
        :feedback1: ('.*',u'¿Realmente ejecutaste el programa?')

        ¿Qué forma dibujará el programa cuando pulses sobre el botón Run?

.. activecode:: Turtle_2
    :tour_1: "Line-by-line Tour"; 1: t1-line1; 2: t1-line2; 3: t1-line3; 4: t1-line4; 5: t1-line5; 6: t1-line6; 7: t1-for100-1; 8: t1-right90-1; 9: t1-for100-2; 10: t1-right90-2; 11: t1-for100-3; 12: t1-right90-3;
    :nocodelens:

    from turtle import *	# usa la biblioteca turtle
    espacio = Screen()    	# crea un espacio de tortugas
    sara = Turtle()   		# crea una tortuga llamada sara
    sara.setheading(90) 	# apunta al norte
    sara.forward(100)   	# mueve a sara hacia delante 100 unidades
    sara.right(90)       	# gira 90 grados
    sara.forward(100)   	# mueve a sara hacia delante 100 unidades
    sara.right(90)       	# gira 90 grados
    sara.forward(100)   	# mueve a sara hacia delante 100 unidades
    sara.right(90)      	# gira 90 grados
    sara.forward(100)    	# mueve a sara hacia delante 100 unidades
    sara.right(90)       	# gira 90 grados

.. note::

    Discute los temas de esta sección con tus compañeros.

      .. disqus::
          :shortname: cslearn4u
          :identifier: studentcsp_1_5
