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
	:prefix: csp-3-8-

.. highlight:: python
   :linenothreshold: 4

Determinar una Factura
====================================

Podemos usar variables para resolver problemas como los que resolveríamos con una hoja de cálculo.  Imagina que tuvieras una hoja de cálculo con una factura para una empresa de suministros de oficina.

.. figure:: Figures/invoice.png
    :width: 600px
    :align: center
    :alt: a spreadsheet
    :figclass: align-center

    Figura 3: Una hoja de cálculo con información del pedido

Aquí está un programa para computar el precio total de la factura.  Asegúrate de pulsar el botón |audiobutton| para entender qué está pasando.

.. activecode:: Invoice1
    :tour_1: "Line by line tour"; 1: inv-line1; 2: inv-line2; 3: inv-line3; 4: inv-line4; 5: inv-line5; 6: inv-line6; 7: inv-line7; 8: inv-line8;

    cantidad1 = 2
    precioUnidad1 = 7.56
    total1 = cantidad1 * precioUnidad1
    cantidad2 = 4
    precioUnidad2 = 4.71
    total2 = cantidad2 * precioUnidad2
    totalFactura = total1 + total2
    print(totalFactura)

.. mchoice:: 3_8_1_Invoice1_Q1
		   :answer_a: 7
		   :answer_b: 6
		   :answer_c: 5
		   :answer_d: 2
		   :correct: a
		   :feedback_a: Si, cantidad1, precioUnidad1, total1, cantidad2, precioUnidad2, total2, totalFactura.
		   :feedback_b: Hay tres variables por línea, dos líneas, y un total.
		   :feedback_c: Hay tres variables por línea, dos líneas, y un total.
		   :feedback_d: Hay tres variables por línea, dos líneas, y un total.

		   ¿Cuántas variables hay en este programa?

Realmente no tenemos que crear nuevas variables ``cantidad2`` y ``precioUnidad2``.  Solo los usamos para computar el total para la línea, y después podríamos reusar los nombres de variable.

.. codelens:: Invoice2

  cantidad = 2
  precioUnidad = 7.56
  total1 = cantidad * precioUnidad
  cantidad = 4
  precioUnidad = 4.71
  total2 = cantidad * precioUnidad
  totalFactura = total1 + total2
  print(totalFactura)

.. mchoice:: 3_8_2_Invoice2_Q1
		   :answer_a: 7
		   :answer_b: 6
		   :answer_c: 5
		   :answer_d: 2
		   :correct: c
		   :feedback_a: Ahora tenemos dos variables menos.
		   :feedback_b: Tenemos el total para cada línea (dos), una cantidad, un precioUnidad, y un totalFactura.
		   :feedback_c: Las variables son cantidad, precioUnidad, total1, total2, y totalFactura.
		   :feedback_d: Tenemos el total para cada línea (dos), una cantidad, un precioUnidad, y un totalFactura.

		   ¿Cuántas variables hay en este programa?

.. Note::
   Es mejor usar nombres de variable que tienen sentido, como ``totalFactura`` y ``cantidad`` en lugar de nombres que no tienen ningún sentido como ``estaVariableEsMiAmiga`` y ``Fred``.  El nombre debería ayudar a recordar qué representa la variable.

Supongamos que las manzanas están a $0.40 la pieza, y las peras a $0.65 la pieza.  Modifica el programa para calcular el coste total.

.. activecode:: Complete_Assignment

   manzanas = 4
   peras = 3
   costeTotal =
   print(costeTotal)

Te animamos a probar las siguientes respuestas copiando y pegando en el programa de arriba antes de contestar esta pregunta:

.. mchoice:: 3_8_3_Make_An_Assignment_Q1
  :answer_a: costeTotal = manzanas + peras
  :answer_b: costeTotal = (0.4 * manzanas) + (0.65 * peras)
  :answer_c: costeTotal = (0.4 * peras) + (0.65 * manzanas)
  :answer_d: costeTotal = (0.4 + manzanas) * (0.65 + peras)
  :correct: b
  :feedback_a: No considera el coste de las manzanas o las peras.
  :feedback_b: Necesitamos multiplicar el coste por manzana por el número de manzanas y sumarlo al coste por pera por el número de peras.
  :feedback_c: Los costes esán al revés.
  :feedback_d: Es una fórmua incorrecta para computar el coste total.

   ¿Qué línea de código computará el ``costeTotal`` correcta si se pone en la línea 3 arriba?

.. tabbed:: 3_8_4_WSt

        .. tab:: Pregunta

           Escribe el código para calcular e imprimir cuántos *clips* puedes comprar si cada clip cuesta $0.05 y tienes $4.00 en tu bolsillo.  Debería imprimir 80.

           .. activecode::  3_8_4_WSq
               :nocodelens:

        .. tab:: Respuesta

            Crea variables para almacenar cada valor.  Calcula ``numClips`` como ``presupuesto / costePorClip``.  Asegúrate de imprimir el resultado.

            .. activecode::  3_8_4_WSa
                :nocodelens:

                # DECLARA VARIABLES Y ASIGNA VALORES
                costePorClip = .05
                presupuesto = 4.00
                # 2. CREA FORMULA
                numClips = presupuesto / costePorClip
                # 3. IMPRIME RESULTADO
                print(numClips)

        .. tab:: Discusión

            .. disqus::
                :shortname: cslearn4u
                :identifier: studentcsp_3_8_4_WSq

.. note::

    Discute los temas tratados en esta sección con tus compañeros.

      .. disqus::
          :shortname: cslearn4u
          :identifier: studentcsp_3_8
