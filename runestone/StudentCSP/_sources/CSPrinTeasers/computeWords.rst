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
	:prefix: csp-1-4-


.. |runbutton| image:: Figures/run-button.png
    :height: 20px
    :align: top
    :alt: run button

.. |audiobutton| image:: Figures/start-audio-tour.png
    :height: 20px
    :align: top
    :alt: audio tour button


Computar con palabras
=====================

..	index::
	single: string
	single: cadena
	pair: programación; cadena

El computador también puede computar con palabras, o de forma más precisa, con **cadenas** (*strings* en inglés) que son secuencias de caracteres.  Podemos crear una **cadena** tecleando caracteres entre un par de comillas simples (``'Hola'``), dobles (``"Hola"``), o triples (``'''Hola'''``).  Podemos "computar" con cadenas usando algunos de los mismos operadores aritméticos -- solo que aquí significan otra cosa.  Aquí generamos la letra de una canción tonta usando ``+`` para combinar (adjuntar) dos cadenas y ``*`` para repetir cadenas.

Bajo el programa, a la derecha del botón *Run* |runbutton|, verás un botón para abrir la audioguía para este programa: |audiobutton|.  Pulsa en ese botón y luego pulsa en "Line-by-line Tour" para escuchar la audioguía.  Puedes usar los botones proporcionados para pausar, oir, saltar o volver.

.. activecode:: String_Operators
  :tour_1: "Line-by-line Tour"; 1: str1-line1; 2: str1-line2; 3: str1-line3; 4: str1-line4; 5: str1-line5; 6: str1-line6; 7: str1-line7; 8: str1-line8; 9: str1-line9; 10: str1-line10;
  :nocodelens:

  basic = "Ma"
  print(basic)
  basic3 = basic + basic + basic
  print(basic3)
  next = "Mow"
  next3 = next * 3
  print(next3)
  together = (basic * 3) + (next * 2)
  print(together)
  print(together + "Mmm" + together)

..	index::
	single: notación punto
	single: dot-notation
	pair: programming; dot-notation
	pair: programación; notación punto

A una cadena se le puede pedir que devuelva una nueva cadena que cambia de alguna forma la cadena original.  En el siguiente ejemplo tomaremos una cadena con todas las letras mayúsculas y la convertiremos en una frase correctamente capitalizada.  Este ejemplo usa la **notación punto** (``frase.lower()``) que es la forma de decirle a la cadena qué queremos que cambie.

.. activecode:: String_Methods
   :tour_1: "Line-by-line Tour"; 1: str2-line1; 2: str2-line2; 3: str2-line3; 4: str2-line4; 5: str2-line5;
   :nocodelens:

   frase = "ESTO ES UNA PRUEBA"
   mejor = frase.lower()
   print(mejor)
   aunMejor = mejor.capitalize() + "."
   print(aunMejor)

.. mchoice:: 1_4_1_String_Methods_Q1
   :answer_a: Hi There
   :answer_b: HiThere
   :answer_c: Hi There Hi There
   :answer_d: HiThereHiThere
   :answer_e: HiThere2
   :correct: d
   :feedback_a: Cuando sumas dos cadenas se copian la segunda cadena a continuación de la primera, sin espacios añadidos
   :feedback_b: Recuerda que * 2 repite dos copias de la misma cadena
   :feedback_c: Sumar dos cadenas y repetirlas no añade espacios entre las cadenas
   :feedback_d: Las cadenas se suman sin añadir ningún espacio y se repiten sin añadir ningún espacio
   :feedback_e: El * 2 repite dos copias de la misma cadena

   What would the following code print?

   ::

      first = "Hi"
      next = "There"
      print ((first + next) * 2)

.. note::

    Discute los temas de esta sección con tus compañeros.

      .. disqus::
          :shortname: uclm-eii-cs
          :identifier: studentcsp_1_4
