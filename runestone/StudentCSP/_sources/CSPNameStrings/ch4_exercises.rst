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
	:prefix: 4-6-

Chapter 4 Exercises
--------------------

#.

    .. tabbed:: ch4ex1t

        .. tab:: Pregunta

            Hay 3 errores de sintaxis en el código siguiente.  Arréglalo para que imprima correctamente sin errores.  Imprimirá "Tu nombre es Carla y tu color favorito es rojo".

            .. activecode:: ch4ex1q
                :nocodelens:

                color = "rojo'
                nombre = 'Carla'
                print("Tu nombre es " + nombre +
                      y tu color favorito es" + color + ".")

        .. tab:: Discusión

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch4ex1q

#.

    .. tabbed:: ch4ex2t

        .. tab:: Pregunta

           Obtendrás un error si intentas ejecutar el código siguiente.  Arréglalo para que imprima correctamente sin errores.  Debería imprimir, "Tu nombre es Carla y tu edad es 5."

           .. activecode::  ch4ex2q
               :nocodelens:

               edad = 5
               nombre = 'Carla'
               print("Tu nombre es" + nombre +
                     "y tu edad es" + edad + ".")

        .. tab:: Discusión

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex2q

#.

    .. tabbed:: ch4ex3t

        .. tab:: Pregunta

           Hay 3 errores de sintaxis en el código siguiente.  Arréglalos para que imprima sin errores.  Imprimirá tu nombre y edad.

           .. activecode::  ch4ex3q
               :nocodelens:

               edad = input("¿Qué edad tienes?")
               nombre = input ("¿Cuál es tu nombre?")
               print ("Tu nombre es " + Nombre
                      " y tienes "  edad "años.")

        .. tab:: Discusión

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch4ex3q

#.

    .. tabbed:: ch4ex4t

        .. tab:: Pregunta

           Modifica la línea 6 para imprimir: "El número de millas que puedes conducir con 25 dólares es 273.97260274."

           .. activecode::  ch4ex4q
               :nocodelens:

               fondos = 25
               millasPorGalon = 40
               precioPorGalon = 3.65
               numGalones = fondos / precioPorGalon
               numMillas = millasPorGalon * numGalones
               print(numMillas)

        .. tab:: Discusión

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex4q

#.

    .. tabbed:: ch4ex5t

        .. tab:: Pregunta

           Modifica la línea 6 para imprimir: "Puedes pedir 40.0 alitas si sois 5 personas, cada uno puede gastar 4 dólares y las alitas cuestan 0.5 dólares la unidad."

           .. activecode::  ch4ex5q
                :nocodelens:

                numPersonas = 5
                gastoPorPersona = 4
                precio = 0.5
                total = numPersonas * gastoPorPersona
                numAlitas =  total / precio
                print(numAlitas)

        .. tab:: Discusión

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex5q

#.

    .. tabbed:: ch4ex6t

        .. tab:: Pregunta

           Combina las líneas 4 y 5 en el código siguiente para imprimir: "270 son 4.0 horas y 30 minutos."

           .. activecode::  ch4ex6q
                :nocodelens:

                totalMinutos = 270
                numMinutos = totalMinutos % 60
                numHours = (totalMinutos - numMinutos) / 60
                print(numHours)
                print(numMinutos)

        .. tab:: Discusión

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex6q

#.

    .. tabbed:: ch4ex7t

        .. tab:: Pregunta

           Completa los cálculos de las líneas 2 y 4 e introduce los elementos a imprimir en la línea 5 para imprimir el número de millas que podrías conducir si tienes un depósito de 10 galones de combustible que solo tiene un cuarto del depósito lleno y tu coche hace 32 millas por galón.  Debería imprimir: "Puedes hacer 80.0 millas."

           .. activecode::  ch4ex7q
                :nocodelens:

                capacidadDeposito = 10
                numGalones =
                millasPorGalon = 32
                numMillas =
                print()

        .. tab:: Discusión

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex7q

#.

    .. tabbed:: ch4ex8t

        .. tab:: Pregunta

           Escribe el código para obtener del usuario el nombre de un color usando la función ``input``.  A continuación convierte el nombre del color a minúsculas e imprímelo.

           .. activecode::  ch4ex8q
                :nocodelens:

        .. tab:: Discusión

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex8q

#.

    .. tabbed:: ch4ex9t

        .. tab:: Pregunta

           Escribe el código necesario para calcular e imprimir cuántos meses se necesitarán para ahorrar $200 si ganas $20 a la semana.  Debería imprimir: "Se necesitan 2.5 meses para ahorrar 200 si ganas 20 dólares a la semana."

           .. activecode::  ch4ex9q
                :nocodelens:

        .. tab:: Discusión

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex9q

#.

    .. tabbed:: ch4ex10t

        .. tab:: Pregunta

           Escribe el código para obtener al menos 3 valores del usuario usando la función ``input`` y sacar una historia mad lib (que usará la entrada para contar una historia tonta).

           .. activecode::  ch4ex10q
               :nocodelens:

        .. tab:: Discusión

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch4ex10q
