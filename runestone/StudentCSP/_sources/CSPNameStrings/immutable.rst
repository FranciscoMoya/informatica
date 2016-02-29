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

.. 	qnum::
	:start: 1
	:prefix: csp-4-3-

Las Cadenas son Inmutables
==========================

..	index::
	pair: string; immutable
	pair: cadena; inmutable

Aunque puedes manipular una cadena para crear una nueva cadena la cadena original es **inmutable** que quiere decir que no cambia.  Date cuenta que después de ejecutar el código de abajo la cadena almacenada en la variable ``frase`` no ha cambiado.

.. activecode:: String_Immutable
   :tour_1: "Line-by-line Tour"; 1: str2-line1; 2: str2-line2; 3: str2-line3; 4: str2-line4; 5: str2-line5; 6: str2-line6;

   frase = "ESTO ES UNA PRUEBA"
   mejor = frase.lower()
   print(mejor)
   aunMejor = aunMejor.capitalize() + "."
   print(aunMejor)
   print(frase)

Aunque las cadenas no pueden ser cambiadas tu puedes cambiar el valor de una variable.  Esto descarta la cadena original y pone el valor de la variable a la nueva cadena.

.. activecode:: String_Reassign
   :tour_1: "Line-by-line Tour"; 1: sa2-line1; 2: sa2-line3; 3: sa2-line2; 4: str2-line6;

   frase = "ESTO ES UNA PRUEBA"
   print(frase)
   frase = "Hola"
   print(frase)

.. mchoice:: 4_3_1_s1
   :answer_a: xyz
   :answer_b: xyxyz
   :answer_c: xy xy z
   :answer_d: xy z
   :answer_e: z
   :correct: b
   :feedback_a: s1 será igual a "xy" mas otro "xy" y después z al final.
   :feedback_b: s1 contiene el valor original, mas ella misma, mas "z"
   :feedback_c: No se añaden espacios durante la concatenación.
   :feedback_d: No se añaden espacios durante la concatenación, y un "xy" adicional debería ser incluído al principio.
   :feedback_e: s1 se asignó a "xy" inicialmente, por tanto la respuesta final será "xyxyz"

   Dado el siguiente fragmento de codigo, ¿Cuál es el valor de s1 tras su ejecución?

   ::

     s1 = "xy"
     s2 = s1
     s1 = s1 + s2 + "z"

.. mchoice:: 4_3_2_s2
   :answer_a: Hey
   :answer_b: hey
   :answer_c: HEY
   :correct: c
   :feedback_a: Sería ciert si hubiéramos preguntado el valor de s3. Cuál es el valor de s1?
   :feedback_b: Sería ciert si hubiéramos preguntado el valor de s2. Cuál es el valor de s1?
   :feedback_c: Las cadenas son inmutables, que significa que no cambian.  Cualquier función que cambia una cadena devuelve una nueva cadena.  Por tanto s1 nunca cambia a no ser que se le asigne una cadena diferente.

   ¿Cuál es el valor de s1 después de ejecutar el siguiente código?

   ::

     s1 = "HEY"
     s2 = s1.lower()
     s3 = s2.capitalize()

.. note::

    Discute los temas tratados en esta sección con tus compañeros.

      .. disqus::
          :shortname: cslearn4u
          :identifier: studentcsp_4_3
