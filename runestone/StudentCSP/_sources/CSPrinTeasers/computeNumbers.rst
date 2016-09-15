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
	:prefix: csp-1-3-


.. |runbutton| image:: Figures/run-button.png
    :height: 20px
    :align: top
    :alt: run button

.. |audiobutton| image:: Figures/start-audio-tour.png
    :height: 20px
    :align: top
    :alt: audio tour button

Computar con números
=====================

No usaremos muchas matemáticas en este eBook, así que no te preocupes si las matemáticas no son tu materia favorita.  Ejecutarás y modificarás programas que trabajan con palabras, tortugas (virtuales, por supuesto), e imágenes además de números.  Las únicas matemáticas que necesitarás son las operaciones de suma, resta, multiplicación y división.

..	index::
	single: variable
	pair: programación; variable

Los computadores se usaron inicialmente para realizar cálculos.  Puede que estés habituado a hacer cálculos con una calculadora, pero los cálculos son a menudo más fáciles si puedes *nombrar* los números con los que trabajas.  Cuando nombras un número, o el resultado de un cálculo, estás creando una **variable**.  Una **variable** es un nombre asociado con una parte de la memoria del computador que contiene un valor, que puede ser cambiado o variar.  Un ejemplo de una **variable** es la puntuación en un juego.  La puntuación empieza en 0 y se incrementa conforme avanzas en el juego.

.. figure:: Figures/pongScore.png
    :width: 400px
    :align: center
    :alt: Un juego en Scratch con una puntuación
    :figclass: align-center

    Figura 2: Una versión del juego pong en `Scratch <http://scratch.mit.edu>`_ con una puntuación arriba a la izquierda.

Una cosa que puedes estar interesado en calcular es el **Índice de Masa Corporal**.    `El Índice de Masa Corporal (IMC) <http://www.nutricion.org/recursos_y_utilidades/calculos_personales.htm>`_ es una medida de la grasa corporal que es útil para monitorizar potenciales problemas de salud.  En términos generales:

- Un IMC de 18.5 o menos se considera *bajo peso*.
- Un IMC entre 18.5 y 24.9 se considera *saludable*.
- Un IMC entre 25 y 29.9 se considera *sobrepeso*.
- Un IMC de 30 o más se considera *obesidad*.

Para calcular el IMC usando unidades británicas necesitarás la altura (en pulgadas) y el peso (en libras).  Eleva al cuadrado la altura (multiplica la altura en pulgadas por sí misma), después divide el peso en libras por la altura al cuadrado.  El IMC se define en unidades del SI (metros y kilogramos), por ello para convertir de libras y pulgadas multiplica el resultado por 703.

En la caja de texto de abajo hay un programa de computador que calcula el IMC para alguien de 60 pulgadas de altura (5 pies) y 110 libras.

Pulsa el botón |runbutton| para hacer que el computador ejecute estos pasos. La salida de este programa se mostrará a la derecha del programa.

Pulsa el botón |audiobutton| para activar un "Audio Tour" que explica el programa línea por línea.

Solo puedes usar los botones *Save* y *Load* si estás registrado en el sistema. El botón *Save* almacenará el programa actual y el botón *Load* cargará el programa almacenado.

.. activecode:: BMI
    :tour_1: "Line-by-line Tour"; 1: BMI-line1; 2: BMI-line2; 3: BMI-line3; 4: BMI-line4; 5: BMI-line5; 6: BMI-line6; 7: BMI-line7;
    :nocodelens:

    altura = 60  # en pulgadas (60 pulgadas son 5 pies)
    peso = 110   # en libras
    cuadradoAltura = altura * altura
    IMC = peso / cuadradoAltura
    IMCmetrico = IMC * 703
    print("IMC:")
    print(IMCmetrico)

Cambia el peso (en libras) y la altura (en pulgadas) en el programa de arriba, después pulsa el botón *Run* para calcular un nuevo IMC.

.. Note
   Fíjate en cómo el nombrado de los valores (usando variables) para altura y peso facilita adivinar qué valores necesitan cambiarse.

.. mchoicemf:: 1_2_1_BMI_Q1
   :answer_a: 21.9
   :answer_b: 21.924704834
   :answer_c: 21
   :answer_d: 22
   :correct: b
   :feedback_a: Cerca, pero el computador te dará más dígitos.
   :feedback_b: ¡Si!
   :feedback_c: No, el resultado será un número con punto decimal y números después del punto.
   :feedback_d: No, el computador no redondea el resultado.

   Imagina que mides 5 pies y 7 pulgadas y pesas 140 libras. ¿Cuál sería tu IMC?

.. note::

    Discute los temas tratados en esta sección con tus compañeros.

      .. disqus::
          :shortname: uclm-eii-cs
          :identifier: studentcsp_1_3
