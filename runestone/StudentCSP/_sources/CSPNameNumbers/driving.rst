..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. |runbutton| image:: Figures/run-button.png
    :height: 20px
    :align: top
    :alt: run button

.. |audiobutton| image:: Figures/start-audio-tour.png
    :height: 20px
    :align: top
    :alt: audio tour button

.. |codelensfirst| image:: Figures/codelens-first.png
    :height: 20px
    :align: top
    :alt: move to first button

.. |codelensback| image:: Figures/codelens-back.png
    :height: 20px
    :align: top
    :alt: back button

.. |codelensfwd| image:: Figures/codelens-forward.png
    :height: 20px
    :align: top
    :alt: forward (next) button

.. |codelenslast| image:: Figures/codelens-last.png
    :height: 20px
    :align: top
    :alt: move to last button

.. 	qnum::
	:start: 1
	:prefix: csp-3-5-

.. highlight:: java
   :linenothreshold: 4

Conducir de Chicago a Dallas
====================================

..	index::
	single: CodeLens

Como ejemplo imagina que estuvieras planeando conducir de Chicago a Dallas. Si sabes cuántas millas por galón hace tu coche, y cuántas millas hay de distancia, podrías estimar el número de galones de combustible que consumiría.

Usa el *CodeLens* a continuación para hacer un seguimiento de lo que implicaría para el ordenador la ejecución de este programa:

- Pulsa |codelensfwd| para avanzar ejecutando una línea del programa.
- Pulsa |codelenslast| para ejecutar todas las líneas del programa.

.. codelens:: Chicago_2_Dallas

   distancia = 924.7
   mpg = 35.5
   galones = distancia / mpg

..	index::
	single: camel case
	single: capitalización de camello

Ahora si conocemos el coste medio de un galón de combustibles, podemos anticipar el coste del viaje de Chicago a Dallas en tu coche.

.. Note::

   Date cuenta de que en el código a continuación usamos nombres de variables como ``costePorGalon`` y ``costeViaje``.  Un nombre de variable no puede contener espacios.  Por tanto una forma de hacer más legible el nombre de una variable cuando contiene más de una palabra es poner en mayúscula la primera letra de cada palabra nueva, como ves en ``costePorGalon`` y ``costeViaje``.  Esto se llama **capitalización de camello** (*camel case* en inglés).  Ten presente que la capitalización importa en Python:  ``costeViaje`` es un nombre diferente a ``costeviaje``.

.. codelens:: Chicago_2_Dallas_Cost

   distancia = 924.7
   mpg = 35.5
   galones = distancia / mpg
   costePorGalon = 3.65
   costeViaje = galones * costePorGalon

..	index::
	single: tracing
	single: string
	single: print
	single: cadena
	single: trazar
	pair: programming; tracing
	pair: programación; trazar

Lo que estamos haciendo arriba es **trazar** un programa.  Normalmente **ejecutamos** un programa -- le decimos al computador que ejecute cada paso del programa tan rápido como sea posible.  Cuando hacemos esto no vemos valores individuales de variables, como pasa arriba.  Podemos comprobar los valores (incluso los valores de variables) imprimiéndolos.  La función ``print`` puede recibir una *entrada* (un nombre de variable entre paréntesis) cuyo valor será mostrado en pantalla.  La función ``print`` también puede imprimir una **cadena** (como ``"Coste de ir de Chicago a Dallas"``) que es una secuencia de caracteres entre un par de comillas dobles como aparece en la línea 6 del código siguiente.  Imprimirá el contenido exacto de la cadena.  Es útil por ejemplo para explicar los valores que estás imprimiendo.

Pulsa el botón |runbutton| a continuación para ver el programa ejecutándose a toda velocidad.

.. activecode:: Trip_Calculator
   :tour_1: "Line by line tour"; 1: trp-line1; 2: trp-line2; 3: trp-line3; 4: trp-line4; 5: trp-line5; 6: trp-line6; 7: trp-line7;

   distancia = 924.7
   mpg = 35.5
   galones = distancia / mpg
   costePorGalon = 3.65
   costeViaje = galones * costePorGalon
   print("Coste de ir de Chicago a Dallas")
   print(costeViaje)

¿Cómo funciona este programa? Prueba a pulsar el botón |audiobutton| para escuchar una explicación del programa.

Prueba a editar el programa anterior y ejecutarlo para contestar la siguiente pregunta:

.. mchoice:: 3_5_1_Chicago_2_Dallas_Q1
   :answer_a: Sí
   :answer_b: No
   :answer_c: Mejor vamos en avión.
   :correct: a
   :feedback_a: Sí, el coste sería de $89.86 (algo que supiste editando el programa anterior y ejecutándolo)
   :feedback_b: Pruébalo -- es ligeramente inferior a $90.
   :feedback_c: Puede que tengas razón, pero anticipa cuál sería el coste editando el programa anterior.

   Si el coste por galón cae a $3.45, ¿podemos conducir de Chicago a Dallas por menos de $90 en combustible?

.. mchoice:: 3_5_2_Chicago_2_Dallas_Q2
   :answer_a: 3.45
   :answer_b: 3.65
   :answer_c: costePorGalon
   :correct: c
   :feedback_a: Sería cierto si estuviera imprimiendo el valor de la variable después de que la cambiaras para averiguar la respuesta a la pregunta anterior.
   :feedback_b: Sería cierto si estuviera imprimiendo el valor original de la variable.
   :feedback_c: Puesto que <code>costePorGalon</code> está entre comillas dobles es una cadena, y por tanto imprimirá exactamente esos caracteres.

   ¿Qué imprimirá ``print("costPerGallon")`` si esta línea fuera añadida al final del último programa?

.. note::

    Discute los temas tratados en esta sección con tus compañeros.

      .. disqus::
          :shortname: cslearn4u
          :identifier: studentcsp_3_5
