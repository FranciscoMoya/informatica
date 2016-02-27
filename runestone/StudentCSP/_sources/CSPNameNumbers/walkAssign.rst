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
	:prefix: csp-3-7-

.. highlight:: java
   :linenothreshold: 4

Pasear por la Asignación con más Generalidad
======================================================

Vamos a explorar la asignación en general.  Prueba a trazar el siguiente ejemplo.

.. codelens:: Assign_Basic

   a = 1
   b = 12.3
   c = "Fred"
   d = b

.. mchoice:: 3_7_1_Assignment_Q1
   :answer_a: 1
   :answer_b: 12.3
   :answer_c: "b"
   :answer_d: "d"
   :correct: b
   :feedback_a: La variable a no se usa en la definición de la variable b.
   :feedback_b: A la variable d se le asigna una copia del valor de la variable b.  La variable b sigue conteniendo el valor 12.3.
   :feedback_c: La variable d tiene asignado el mismo valor que el almacenado en b.
   :feedback_d: La variable d toma su valor de la variable b.

   ¿Cuál es el valor de la variable ``d`` cuando este programa termine de ejecutarse?

La *secuencia* de sentencias en un programa es muy importante.  La asignación no crea ninguna clase de relación entre los nombres, como en matemáticas.  La variable ``a`` podría ser igual a ``12`` en un punto, y ``15`` en otro.  Una sentencia de asignación es una acción que ocurre una sola vez y una vez ejecutada se pasa página.

.. codelens:: Assign_Multiple

	    var1 = 45
	    var1 = 17.3
	    var2 = var1

.. mchoice:: 3_7_2_Assignment_Multiple_Q1
		   :answer_a: var1 es 45, var2 es 45
		   :answer_b: var1 es 45, var2 es var1
		   :answer_c: var1 es 17.3, var2 es 45
		   :answer_d: var1 es 17.3, var2 es 17.3
		   :correct: d
		   :feedback_a: La variable var1 se asignó a 45, pero se cambia en la línea 2, antes de que var2 tome un valor.
		   :feedback_b: Ambas variables contienen valores numéricos, porque son los únicos valores en este programa.
		   :feedback_c: La variable var2 nunca se pone a 45 en este programa.
		   :feedback_d: La variable var1 se pone inicialmente a 45 y después se cambia a 17.3, y después var2 toma el valor de var1.

		   ¿Cuáles son los valores de ``var1`` y ``var2`` después de ejecutar este programa?

Podemos ver valores (incluyendo los valores de variables con nombre) imprimiéndolos.   Es una forma útil para ver qué está pasando en el programa.  Prueba a ejecutar este ejemplo donde hacemos que el computador calcule el número de días que hay en tres semanas:

.. activecode:: Assign_Days
   :tour_1: "Line by line tour"; 1: calcDays-line1; 2: calcDays-line2; 3: calcDays-line3; 4: calcDays-line4; 5: calcDays-line5; 6: calcDays-line6;

   diasPorSemana = 7
   print(diasPorSemana)
   numDias = 7 * 3
   print(numDias)
   numDias2 = diasPorSemana * 3
   print(numDias2)

.. mchoice:: 3_7_3_Assign_Days_Q1
		   :answer_a: 7, 7*3, diasPorSemana*3
		   :answer_b: diasPorSemana, numDias, numDias2
		   :answer_c: 7, 21, 21
		   :answer_d: 7, 21, 3
		   :correct: c
		   :feedback_a: Los valores serán realmente calculados y se imprimirán números.
		   :feedback_b: Los nombres de variable no se imprimirán.
		   :feedback_c: El primer print imprimirá el valor de diasPorSemana (7), el segundo el valor de numDias (21), y el tercero el valor de numDias2 (21).
		   :feedback_d: El valor de diasPorSemana será computado y asignado.

		   ¿Qué tres valores se imprimirán cuando se ejecute este programa?

.. parsonsprob:: 3_7_4_Per_Person_Cost

   El siguiente programa debería calcular el coste por persona de una cena incluída la propina.  Pero los bloques están desordenados.  Arrastra los bloques de la izquierda y sitúalos en el orden correcto en la derecha.  Pulsa el botón <i>Check Me</i> para comprobar tu solución.</p>
   -----
   cuenta = 89.23
   =====
   propina = cuenta * 0.20
   =====
   total = cuenta + propina
   =====
   numPersonas = 3
   costePorPersona = total / numPersonas
   =====
   print(costePorPersona)

.. tabbed:: 3_7_5_WSt

        .. tab:: Pregunta

           10 personas fueron a un restaurante a cenar.  Cada comensal tomó un aperitivo y un primer plato.  Todos compartieron un postre.  Escribe el código para calcular e imprimir la *cuenta* total si cada aperitivo cuesta $2.00, cada primer plato cuesta $9.89, y el postre cuesta $7.99.  Debería imprimir 126.89.

           .. activecode::  3_7_5_WSq
               :nocodelens:

        .. tab:: Respuesta

            Crea variables para contener cada valor.  Calcula ``cuentaTotal`` como ``costeAperitivos + costePrimeros + costePorPostre``.  Asegúrate de imprimir el resultado.

            .. activecode::  3_7_5_WSa
                :nocodelens:

                # DECLARA VARIABLES Y ASIGNA VALORES
                costePorAperitivo = 2.00
                costePorPrimero = 9.89
                costePorPostre = 7.99
                # CREA FORMULA PARA CALCULAR CUENTA
                costeAperitivos = costePorAperitivo * 10
                costePrimeros = costePorPrimero * 10
                cuentaTotal = costeAperitivos + costePrimeros + costePorPostre
                # IMPRIME EL RESULTADO
                print(cuentaTotal)

        .. tab:: Discusión

            .. disqus::
                :shortname: cslearn4u
                :identifier: studentcsp_3_7_5_WSq

.. note::

    Discute los temas tratados en esta sección con tus compañeros.

      .. disqus::
          :shortname: cslearn4u
          :identifier: studentcsp_3_7
