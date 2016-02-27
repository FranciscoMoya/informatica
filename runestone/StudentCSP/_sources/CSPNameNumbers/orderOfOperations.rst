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
	:prefix: csp-3-4-

.. highlight:: java
   :linenothreshold: 4


Cómo se Evalúan las Expresiones
===============================

El orden en que las expresiones se ejecutan es el mismo que en matemáticas y se muestra en la siguiente tabla desde la precedencia más alta a la más baja.  Si dos símbolos tienen la misma precedencia se evalúan de izquierda a derecha.

+------------------------+----------------------------------------------------+
|Operador                | Nombre                                             |
+------------------------+----------------------------------------------------+
| -x                     | Negación                                           |
+------------------------+----------------------------------------------------+
| x * y, x / y, x % y    | Multiplicación, División, y Módulo                 |
+------------------------+----------------------------------------------------+
| x + y, x - y           | Suma y Resta                                       |
+------------------------+----------------------------------------------------+

.. fillintheblank:: 3_4_1_Order1_fill

    .. blank:: 3_4_1_Order1
        :correct: ^-2$
        :feedback1: ('.*','¿Realmente ejecutaste el programa?')

        ¿Qué se imprimirá cuando pulses en el botón Run del código siguiente?

.. activecode:: Expression_Order1
    :nocodelens:

    result = 4 + -2 * 3
    print(result)

Puedes cambiar el orden por defecto añadiendo paréntesis alrededor de parte de una expresión.

.. fillintheblank:: 3_4_2_Order2_fill

    .. blank:: 3_4_1_Order2
        :correct: ^6$
        :feedback1: ('.*','¿Realmente ejecutaste el programa?')

        ¿Qué se imprimirá cuando pulses en el botón Run del código siguiente?

.. activecode:: Expression_Order2
    :nocodelens:

    result = (4 + -2) * 3
    print(result)

.. note::

    Discute los temas tratados en esta sección con tus compañeros.

      .. disqus::
          :shortname: cslearn4u
          :identifier: studentcsp_3_4
