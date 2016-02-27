..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


.. setup for automatic question numbering.

.. 	qnum::
	:start: 1
	:prefix: csp-3-10-

Capítulo 3 Ejercicios
----------------------

#.

    .. tabbed:: ch3ex1t

        .. tab:: Pregunta

            Escribe lo que piensas que cada una de estas imprimiría, después usa la ventana de código activo para comprobar tus resultados:

            #. ``9 * 5``
            #. ``2 / 5``
            #. ``5 % 2``
            #. ``9 % 5``
            #. ``6 % 6``
            #. ``2 % 7``
            #. ``3 / 0``

            .. activecode:: ch3_ex1
                :nocodelens:

               print(9 * 5)

        .. tab:: Discusión

            .. disqus::
                :shortname: cslearn4u
                :identifier: studentcsp_ch3ex1q

#.

    .. tabbed:: ch3ex2t

        .. tab:: Pregunta

           Añade paréntesis a la expresión ``x = 6 * 1 - 2`` para que el código siguiente imprima -6 en lugar de 4.

           .. activecode::  ch3ex2q
               :nocodelens:

               x = 6 * 1 - 2
               print(x)

        .. tab:: Discusión

            .. disqus::
                :shortname: cslearn4u
                :identifier: studentcsp_ch3ex2q

#.

    .. tabbed:: ch3ex3t

        .. tab:: Pregunta

           Completa el código de las líneas 3 y 5 a continuación para imprimir el coste de un viaje en coche de 500 millas sabiendo que el coche hace 26 millas por galón y el combustible cuesta 3.45 por galón.  Debería imprimir 66.3461538462.

           .. activecode::  ch3ex3q
               :nocodelens:

               millas = 500
               millasPorGalon = 26
               numGalones =
               precioPorGalon = 3.45
               total =
               print(total)

        .. tab:: Discusión

            .. disqus::
                :shortname: cslearn4u
                :identifier: studentcsp_ch3ex3q

#.

    .. tabbed:: ch3ex4t

        .. tab:: Pregunta

           Completa el código de las líneas 4 y 5 para imprimir cuántas millas puedes conducir con $25 si tu coche hace 40 millas por galón y el precio del combustible es $3.65 por galón.  Debería imprimir 273.97260274.

           .. activecode::  ch3ex4q
               :nocodelens:

               fondos = 25
               millasPorGalon = 40
               precioPorGalon = 3.65
               numGalones =
               numMillas =
               print(numMillas)


        .. tab:: Discusión

            .. disqus::
                :shortname: cslearn4u
                :identifier: studentcsp_ch3ex4q

#.

    .. tabbed:: ch3ex5t

        .. tab:: Pregunta

           Completa el código de las líneas 3 y 7 par imprimir el coste final de un elemento que tiene un precio de $68, pero tiene un descuento del 40% de su precio original y adicionalmente tienes un cupón para ahorrar un 20% del precio de venta.  Debería imprimir 32.64.

           .. activecode::  ch3ex5q
                :nocodelens:

                precio = 68
                descuento = 0.4
                rebajaVenta =
                precioVenta = precio - rebajaVenta
                descuento = 0.2
                rebajaCupon = precioVenta * descuento
                precioCupon =
                print(precioCupon)

        .. tab:: Discusión

            .. disqus::
                :shortname: cslearn4u
                :identifier: studentcsp_ch3ex5q

#.

    .. tabbed:: ch3ex6t

        .. tab:: Pregunta

           Termina el código de las líneas 4 and 5 para imprimir cuántas alas se pueden comprar entre 5 personas si cada una puede gastar $4 y las alas cuestan $0.50 cada una. Debería imprimir 40.0.

           .. activecode::  ch3ex6q
                :nocodelens:

                numPersonas = 5
                cantidadPorPersona = 4
                precio = 0.5
                total =
                numAlas =
                print(numAlas)

        .. tab:: Discusión

            .. disqus::
                :shortname: cslearn4u
                :identifier: studentcsp_ch3ex6q

#.

    .. tabbed:: ch3ex7t

        .. tab:: Pregunta

           Termina el código de las líneas 2 y 3 a continuación para imprimir cuántas horas y minutos has estado esperando si en total has estado esperando 270 minutos.  Recuerda que hay 60 minutos en una hora.  Debería imprimir 4.0 y luego 30.

           .. activecode::  ch3ex7q
                :nocodelens:

                totalMinutos = 270
                numMinutos =
                numHoras =
                print(numHoras)
                print(numMinutos)

        .. tab:: Discusión

            .. disqus::
                :shortname: cslearn4u
                :identifier: studentcsp_ch3ex7q

#.

    .. tabbed:: ch3ex8t

        .. tab:: Pregunta

           Arragla los errores de sintaxis en el código siguiente de manera que calcule e imprima el número de horas de trabajo que necesitarás si ganas $8 por hora y quieres ganar $100.  Debería imprimir 12.5.

           .. activecode::  ch3ex8q
                :nocodelens:

                8 = pagaPorHora
                pagaTotal = 100
                pagaTotal / pagaPorHora = numHoras
                print(numHoras)

        .. tab:: Discusión

            .. disqus::
                :shortname: cslearn4u
                :identifier: studentcsp_ch3ex8q

#.

    .. tabbed:: ch3ex9t

        .. tab:: Pregunta

           Termina las líneas 5 y  del código de abajo para imprimir cuantas manzanas puedes comprar si las manzanas cuestan $0.60 cada una, quieres 3 peras que cuestan $1.2 cada una y tienes $8.00.  Debería imprimir 7.33333333333.  Puesto que no puedes comprar 7.333 manzanas ¿puedes encontrar la forma de hacer que imprima solo 7?

           .. activecode::  ch3ex9q
                :nocodelens:

                precioPorManzana = 0.6
                numPeras = 3
                precioPorPera = 1.2
                fondos = 8
                fondosDespuesPeras =
                numManzanas =
                print(numManzanas)

        .. tab:: Discusión

            .. disqus::
                :shortname: cslearn4u
                :identifier: studentcsp_ch3ex9q

#.

    .. tabbed:: ch3ex10t

        .. tab:: Pregunta

           Escribe el código para calcular e imprimir cuantas *millas* puedes conducir si tu coche puede llevar hasta 10 galones de combustible, te queda un cuarto de depósito y tu coche hace 32 millas por galón.  Debería imprimir 80.

           .. activecode::  ch3ex10q
               :nocodelens:

        .. tab:: Discusión

            .. disqus::
                :shortname: cslearn4u
                :identifier: studentcsp_ch3ex10q
