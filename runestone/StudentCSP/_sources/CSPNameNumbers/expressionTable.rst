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
	:prefix: csp-3-3-

.. highlight:: python
   :linenothreshold: 4



Resumen de Tipos de Expresión
=============================

+------------+-------------------------------------------------------------------------------------------------+
| Expresión  | Significado Aritmético                                                                          |
+------------+-------------------------------------------------------------------------------------------------+
| 1 + 2      | Suma, el resultado es 3                                                                         |
+------------+-------------------------------------------------------------------------------------------------+
| 3 * 4      | Multiplicación, el resultado es 12                                                              |
+------------+-------------------------------------------------------------------------------------------------+
| 1 / 3      | División entera, el resultado es 0 en Python antiguo, pero 0.333333333333 en Python 3           |
+------------+-------------------------------------------------------------------------------------------------+
| 2.0 / 4.0  | División, el resultado es 0.5, puesto que estás usando números con decimales en el cálculo      |
+------------+-------------------------------------------------------------------------------------------------+
| 2 % 3      | Módulo (resto), el resultado es 2                                                               |
+------------+-------------------------------------------------------------------------------------------------+
| -1         | Negación, el resultado es -1                                                                    |
+------------+-------------------------------------------------------------------------------------------------+

.. mchoice:: 3_3_1_intDiv_Q1
   :answer_a: 0
   :answer_b: 1
   :answer_c: 0.75
   :answer_d: 0.25
   :correct: c
   :feedback_a: Si los dos valores son enteros (sin decimales) obtendrás normalmente un resultado entero (sin decimales) en entornos antiguos de Python.  Pero este libro usa Python 3 por lo que obtendrás un resultado con decimales.
   :feedback_b: Sería correcto si el resultado se redondeara antes de truncar la parte decimal, pero no hace esto.
   :feedback_c: Aunque no es ésto lo que devolvería un entorno de Python antiguo, en este libro usamos Python 3 por lo que retorna un resultado con decimales.
   :feedback_d: Sería correcto si fuera <code>1 / 4</code>, <code>1.0 / 4</code>, o <code>1 / 4.0</code>

   ¿Cuál es el resultado de ``3 / 4``?

.. mchoice:: 3_3_2_mod_Q1
   :answer_a: 0
   :answer_b: 1
   :answer_c: 2
   :answer_d: 3
   :correct: d
   :feedback_a: Sería correcto si fuera <code>18 % 2</code>, pero ¿cuál es el resto de 18 dividido por 5?
   :feedback_b: Sería correcto si fuera <code>18 % 17</code>, puesto que 17 cabe en 18 una vez el resto es 18 - 17 = 1.
   :feedback_c: ¿Cuál es el mayor múltiplo de 5 que es menor o igual que 18? El resto es 18 - ese número.
   :feedback_d: El resto es 3 puesto que 5 cabe en 18 tres veces (15) y 18 - 15 = 3.

   ¿Cuál es el resultado de ``18 % 5``?

.. mchoice:: 3_3_3_mod_Q2
   :answer_a: 0
   :answer_b: 1
   :answer_c: 2
   :answer_d: 6
   :correct: c
   :feedback_a: Sería correcto si fuera <code>6 % 2</code>.
   :feedback_b: Sería correcto si fuera un número impar dividido por 2, pero no lo es.
   :feedback_c: 6 cabe en 2 cero veces dejando 2 de resto.
   :feedback_d: Si tienes un número más pequeño dividido por uno más grande el resto es siempre el más pequeño.

   What is the result of ``2 % 6``?

.. note::

    Discute los temas tratados en esta sección con tus compañeros.

      .. disqus::
          :shortname: uclm-eii-cs
          :identifier: studentcsp_3_3
