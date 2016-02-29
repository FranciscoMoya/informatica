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
	:prefix: csp-4-4-

Haciendo una Historia MadLib
===================================

Puede que hayas hecho historias MadLib cuando en tu niñez.  Proporcionas algunos piezas de informacion, como el nombre un amigo, un verbo, y tu juego favorito (por ejemplo), y esas piezas se conectan en una historia.  Como no sabes la historia a priori, te sorprendes de lo que le pasa a tu amigo en la historia.

.. activecode:: Story1
   :tour_1: "Line by line tour"; 1: StEx-line1; 2: StEx-line2; 3: StEx-line3; 4: StEx-line4; 5: StEx-line5; 6: StEx-line6; 7: StEx-line7; 8: StEx-line8; 9: StEx-line9; 10: StEx-line10; 11: StEx-line11; 12: StEx-line12; 13: StEx-line13; 14: StEx-line14; 15: StEx-line15;
   :tour_2: "Structural tour"; 1-5: StEx-line1-5; 6-10: StEx-line6-10; 11-15: StEx-line11-15;

   nombre = "Pat"
   apellido = "Smith"
   persona = "chica"
   direccion = "65 Elm Street"
   verbo = "comerse a"
   inicio = "Había una vez una " + persona + " llamada " + nombre + "."
   siguiente1 = "Una buena " + persona + " que vivía en " + direccion + "."
   siguiente2 = "Un día, una malvada bruja vino a la casa de los " + apellido + "."
   siguiente3 = "¡La malvada bruja pretendía " + verbo + " " + nombre + "!"
   final = "Pero " + nombre + " era muy inteligente y se libró de la malvada bruja."
   print(inicio)
   print(siguiente1)
   print(siguiente2)
   print (siguiente3)
   print(final)


.. mchoice:: 4_4_1_Story1_Q1
   :answer_a: finalReal = nombre + " llamó a la policía que se llevó a la bruja."
   :answer_b: print(nombre + " llamó a la policía que se llevó a la bruja.")
   :answer_c: print("Pat llamó a la policía que se llevó a la bruja.")
   :correct: b
   :feedback_a: Solo funcionaría si además se añadiera <code>print(finalReal)</code> después.
   :feedback_b: Esta es una buena forma de hacerlo puesto que la línea tendría el nombre correcto.  También podrías hacer una cadena llamada <code>finalReal</code> primero, y después imprimirla.
   :feedback_c: Esto <i>funcionaría</i>.  Pero si cambias la variable <code>nombre</code> esta línea no cambiaría.  Otra respuesta es mejor.

   Ahora quieres añadir más a la historia. Quieres decir: "Pat llamó a la policía que se llevó a la bruja."  ¿Añadiendo cuál de estas líneas al final del programa se conseguiría? (Sugerencia: ¡Se permite *probar* con cada una!)


**Deberías hacer esto realmente:** Ejecuta este programa para ver qué se genera, después cambia algunas variables para hacer historias diferentes.  Prueba con nombres diferentes y verbos diferentes.


.. activecode:: Story2
   :tour_1: "Line by line tour"; 1: story-line1; 2: story-line2; 3: story-line3; 4: story-line4; 5: story-line5; 6: story-line6; 7: story-line7; 8: story-line8; 9: story-line9; 10: story-line10; 11: story-line11; 12: story-line12; 13: story-line13; 14: story-line14; 15: story-line15;

   nombre = "Sofía"
   apellido = "Díaz"
   persona = "chica"
   direccion = "1600 Pennsylvania Avenue"
   verbo = "eructar hacia"
   inicio = "Había una vez una " + persona + " llamada " + nombre + "."
   siguiente1 = "Una buena " + persona + " que vivía en " + direccion + "."
   siguiente2 = "Un día, una malvada bruja vino a la casa de los " + apellido + "."
   siguiente3 = "¡La malvada bruja pretendía " + verbo + " " + nombre + "!"
   final = "Pero " + nombre + " era muy inteligente y se libró de la malvada bruja."
   print(inicio)
   print(siguiente1)
   print(siguiente2)
   print(siguiente3)
   print(final)

.. mchoice:: 4_4_2_Story2_Q1
   :answer_a: Si
   :answer_b: No
   :correct: a
   :feedback_a: La única diferencia es cuándo se imprimen las líneas, pero las líneas son las mismas.
   :feedback_b: ¿Lo has probado? Copia el código en el área de arriba y ejecútalo.

   ¿Imprimiría el siguiente código la misma historia que el anterior?

   ::

      nombre = "Sofía"
      apellido = "Díaz"
      persona = "chica"
      direccion = "1600 Pennsylvania Avenue"
      verbo = "eructar hacia"
      inicio = "Había una vez una " + persona + " llamada " + nombre + "."
      print(inicio)
      siguiente1 = "Una buena " + persona + " que vivía en " + direccion + "."
      print(siguiente1)
      siguiente2 = "Un día, una malvada bruja vino a la casa de los " + apellido + "."
      print(siguiente2)
      siguiente3 = "¡La malvada bruja pretendía " + verbo + " " + nombre + "!"
      print(siguiente3)
      final = "Pero " + nombre + " era muy inteligente y se libró de la malvada bruja."
      print(final)


.. mchoice:: 4_4_3_StringVsVariableName
   :answer_a: Mali es Mali
   :answer_b: Mali es 5
   :answer_c: 5 es Mali
   :answer_d: 5 es 5
   :correct: b
   :feedback_a: No hay comillas alrededor del último Mali por lo que usará el valor de la variable Mali.
   :feedback_b: El primer Mali está entre dobles comillas por lo que imprimirá la cadena Mali y el segundo Mali no está entre comillas por lo que imprimirá el valor de la variable Mali.
   :feedback_c: El primer Mali está entre dobles comillas y el segundo no.
   :feedback_d: El primer Mali está entre dobles comillas por lo que es una cadena y los caracteres de la cadena se imprimirán.

   ¿Qué imprimiría el siguiente código?

   ::

     Mali = 5
     print("Mali" + " es " + str(Mali))

.. Note::
   Cuando imprimes una cadena (una secuencia de caracteres entre comillas simples, dobles o triples) en Python imprimirá los caracteres exactos de la cadena.  Cuando imprimes una variable imprimirá el valor de esa variable.

.. parsonsprob:: 4_4_4_Poem

   Pon los bloques a continuación en el orden correcto para imprimir un cuarteto de Béquer.
   -----
   print("Por una mirada, un mundo;")
   =====
   print("por una sonrisa, un cielo;")
   =====
   print("por un beso...¡yo no sé")
   =====
   print("que te diera por un beso.")

.. parsonsprob:: 4_4_5_Story

   Pon los bloques a continuación en el orden correcto para declarar las variables y después imprimir la siguiente historia: <i>Un día Jay se fue de compras.  Quería comprar zapatos.  Pero no le gustó ninguno. Así que Jay se fue a casa.</i>
   -----
   name = "Jay"
   item = "zapatos"
   =====
   print("Un día " + name + " se fue de compras.")
   =====
   print("Quería comprar " + item + ".")
   =====
   print("Pero no le gustó ninguno.")
   =====
   print("Así que " + name + " se fue a casa.")

.. tabbed:: 4_4_6_WSt

        .. tab:: Pregunta

           Escribe abajo el código para calcular e imprimir cuántas manzanas puedes recorrer en una hora andando si caminas a un ritmo de .3 manzanas por minuto.  Debería imprimir "Recorreré 18 manzanas en una hora si camino a .3 manzanas por minuto."

           .. activecode::  4_4_6_WSq
                :nocodelens:

        .. tab:: Respuesta

            Nombra cada uno de los valores.  Calcula ``totalManzanas`` e imprime la información.

            .. activecode::  4_4_6_WSa
                :nocodelens:

                # DECLARA VARIABLES
                manzanasPorMinuto = .3
                minutosPorHora = 60
                # CREA FORMULA
                totalManzanas = manzanasPorMinuto * minutosPorHora
                # PROCESA Y MUESTRA RESULTADO
                print("Recorreré " + str(totalManzanas) + " manzanas en una hora si camino a " + str(manzanasPorMinuto) + " manzanas por minuto.")

        .. tab:: Discusión

            .. disqus::
                :shortname: cslearn4u
                :identifier: studentcsp_4_4_6_WSq
.. note::

    Discute los temas tratados en esta sección con tus compañeros.

      .. disqus::
          :shortname: cslearn4u
          :identifier: studentcsp_4_4
