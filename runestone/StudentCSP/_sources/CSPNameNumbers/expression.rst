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
	:prefix: csp-3-2-

.. highlight:: python
   :linenothreshold: 4



Expresiones
=============

..	index::
	single: expressions
	single: arithmetic expressions
	single: expresiones
	single: expresiones aritméticas

El *lado derecho* de la asignación no tiene por qué ser un valor.  Puede ser una *expresión aritmética*, como ``2*2``.  La expresión será evaluada y el resultado de la expresión se almacenará en la variable.

.. fillintheblank:: 3_2_1_Mult_fill

    .. blank:: 3_2_1_Mult
        :correct: ^4$
        :feedback1: ('.*',u'¿Realmente ejecutaste el programa?')

        ¿Qué se imprimirá cuando pulses en el botón Run del código siguiente?

.. activecode:: Expression_Mult
    :tour_1: "Line-by-line Tour"; 1: ex1-line1; 2: ex1-line2;
    :nocodelens:

    result = 2 * 2
    print(result)

División Entera
-------------------

..	index::
	single: integer division
	single: división entera

Puedes usar todos los símbolos matemáticos estándar.

.. fillintheblank:: 3_2_2_Div_fill

    .. blank:: 3_2_2_Div
        :correct: ^0.333333333333$
        :feedback1: ('.*',u'¿Realmente ejecutaste el programa?')

        ¿Qué se imprimirá cuando pulses en el botón Run del código siguiente?

.. activecode:: Expression_Div
    :tour_1: "Line-by-line Tour"; 1: ex2-line1; 2: ex1-line2;
    :nocodelens:

    result = 1 / 3
    print(result)

.. note::
   Este libro utiliza Python 3.x que revuelve un valor con decimales de un cálculo entero como ``1 / 3``.  Si hubiéramos ejecutado ``1 / 3`` en un entorno de desarrollo de Python más antiguo habría impreso ``0``.  En muchos lenguajes si solo se usan enteros en un cálculo (números sin decimales, como -3, 65, -39028, 602939) el resultado será también un entero y la parte fraccionaria (a parte después del punto decimal) se descarta.  En esos entornos es importante usar valores con decimales (como ``1.0 / 2``, ``1 / 2.0``, o ``1.0 / 2.0``) si se desean resultados con decimales.

Módulo
---------

..	index::
	single: módulo
	single: resto
	single: modulo
	single: remainder

También hay símbolos que pueden ser usados de formas que no esperas.

.. fillintheblank:: 3_2_3_Mod_fill

    .. blank:: 3_2_3_Mod
        :correct: ^0$
        :feedback1: ('.*',u'¿Realmente ejecutaste el programa?')

        ¿Qué se imprimirá cuando pulses en el botón Run del código siguiente?

.. activecode:: Expression_Mod
    :tour_1: "Line-by-line Tour"; 1: ex3-line1; 2: ex1-line2;
    :nocodelens:

    result = 4 % 2
    print(result)

Puede que no estés familiarizado con el operador **modulo** (resto) ``%``.  Devuelve el resto de la división del primer número por el segundo.  Probablemente lo hiciste hace tiempo cuando aprendías la división larga.  En el caso de ``4 % 2``, ``2`` cabe en ``4`` dos veces con un resto de ``0``.  El resultado de ``5 % 2`` sería ``1``, puesto que ``2`` cabe en ``5`` dos veces con un resto de ``1``.  De hecho puedes comprobar si el resultado de ``X % 2`` es igual a ``1`` para ver si ``X`` is impar y si el resultado de ``X % 2`` es ``0`` cuando ``X`` es par.

.. figure:: Figures/mod-py.png
    :width: 150px
    :align: center
    :figclass: align-center

    Figura 3: División larga mostrando la parte entera y el resto

.. note::
   El resultado de ``x % y`` cuando ``x`` es más pequeño que ``y`` es siempre ``x``.  El valor de ``y`` no cabe en ``x`` puesto que ``x`` es más pequeño que ``y``, por tanto el resultado es ``x``.  Por tanto si ves ``2 % 3`` el resultado es ``2``.  Edita el código previo para probar esto por tí mismo.  Cambia el código a ``result = 2 % 3`` y mira qué imprime cuando se ejecuta.

.. note::

    Discute los temas tratados en esta sección con tus compañeros.

      .. disqus::
          :shortname: uclm-eii-cs
          :identifier: studentcsp_3_2
