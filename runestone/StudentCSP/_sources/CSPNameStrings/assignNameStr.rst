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
	:prefix: csp-4-1-

Asignar Nombres a Cadenas
===========================

..	index::
	single: assignment
	single: string
	pair: strings; assignment
	single: function
	single: concatenate
	single: append
	single: asignación
	single: cadena
	pair: cadenas; asignación
	single: función
	single: concatenar
	single: añadir

*Objetivos de Aprendizaje:*

- Crear una variable que puede almacenar texto (una cadena).
- Sumar (añadir o concatenar) cadenas para crear nuevas cadenas.
- Introducir la función ``input`` y el concepto de función.
- Convertir un número en una cadena para concatenarla a otra cadena.
- Usar la notación punto para invocar funciones en objetos cadena.
- Introducir algunas funciones de cadenas como ``lower``, ``capitalize``, ``len``, y ``find``.
- Mostrar que las cadenas son inmutables (no cambian).

Concatenar (Añadir) Cadenas
-----------------------------------

Los computadores pueden usar nombres para representar *cualquier cosa*.  En el último capítulo vimos que podemos nombrar números (declarar una variable y poner un valor numérico).  Entonces podemos hacer cálculos usando los nombres de los números.  También podemos nombrar **cadenas** y hacer cálculos con sus nombres.  Una **cadena** (*string* en inglés) es una secuencia de caracteres entre un par de comillas simples, dobles o triples, como ``'Hi'``, ``"¿Qué tal?"``, o ``'''¿Por qué no puedo hacer eso?'''``.  ¿Qué significa hace un cálculo con una cadena?  Bien, Python usa el símbolo ``+`` para **concatenar** cadenas como se muestra a continuación.  **Concatenar** significa crear una nueva cadena con todos los caracteres de la primera cadena seguidos de todos los caracteres de la segunda cadena.  También se le llama **añadir** cadenas.

.. activecode:: String_Assign
   :tour_1: "Line-by-line Tour"; 1: sa1-line1; 2: sa1-line2; 3: sa1-line3; 4: sa1-line4;

   nombre = "Jorge"
   apellido = "Garcia"
   nombreCompleto = nombre + " " + apellido
   print(nombreCompleto)

Ahora prueba a ejecutar este ejemplo ligeramente diferente.

.. activecode:: String_Assign2

   nombre = "Jorge"
   apellido = "Garcia"
   nombreCompleto = nombre + apellido
   print(nombreCompleto)

.. note::
   Los espacios en blanco no se añaden de forma automática cuando concatenas dos cadenas.  Si quieres un espacio en blanco en medio ponlo explćitamente usando una cadena con un solo espacio en ella ``" "`` como aparece en ActiveCode1.

Prueba a ejecutar el ejemplo a continuación.  Debería dar errores. ¿Cómo puedes arreglar los errores?

.. activecode:: String_Assign3

   nombre = 'Jorge"
   apellido = 'Garcia"
   nombreCompleto = nombre " " apellido
   print(nombreCompleto)

.. note::
   Una cadena es una secuencia de caracteres entre un par de comillas simples, dobles o triples.  Si empiezas la cadena con una comilla simple debes acabarla con una comilla simple.  Si empiezas con una comilla doble debes acabarla con una comilla doble.  Tienes que usar el operador ``+`` para concatenar cadenas.

We can use the ``input`` **function** in Python to get your first and last name and then print your full name.  A **function** can take input and returns some value.

.. activecode:: String_Input

   nombre = input("¿Cuál es tu nombre de pila?")
   apellido = input("¿Cuál es tu apellido?")
   nombreCompleto = nombre + " " + apellido
   print("Tu nombre completo es " + nombreCompleto)

Concatenar Cadenas y Números
-----------------------------------

Puedes imprimir tanto cadenas como números, y puedes concatenar cadenas usando ``+``, pero si pruebas a concatenar una cadena y un número obtendrás un error.  La cadena ``"5"`` se almacena en la memoria del ordenador de forma muy diferente al número ``5``.  Por tanto para concatenar el número ``5`` y una cadena tenemos que convertir el número en una cadena antes.  La función ``str(num)`` convertirá un número en una cadena.

.. activecode:: String_Convert
   :tour_1: "Line-by-line Tour"; 1: sa3-line1; 2: sa3-line2; 3: sa3-line3; 4: sa3-line4;

   Fred = 5
   print("Fred")
   print(Fred)
   print("Fred" + " is " + str(Fred))

.. note::
   Date cuenta cómo imprimir la cadena ``"Fred"`` imprime algo completamente diferente que imprimir el valor de la variable ``Fred``.  Imprimir la cadena ``"Fred"`` imprime los caracteres exactos de esa cadena.  Recuerda que las cadenas están rodeades por un par de comillas simples o dobles y que cuando se imprimen se imprimen los caracteres exactos de la cadena.  Cuando imprimes una variable imprimirá el *valor* de esa variable.

Podemos actualizar nuestro ejemplo de viaje en coche para imprimir el coste del viaje con una sola sentencia ``print``.

.. activecode:: Trip_Calculator2
   :tour_1: "Line by line tour"; 1: trp-line1; 2: trp-line2; 3: trp-line3; 4: trp-line4; 5: trp-line5; 6: trp2-line6;

   distancia = 924.7
   mpg = 35.5
   galones = distancia / mpg
   costePorGalon = 3.65
   costeViaje = galones * costePorGalon
   print("Coste de ir de Chicago a Dallas: $" + str(costeViaje))

**Comprueba tu entendimiento**

.. mchoice:: 4_1_1_stringVsValue
   :answer_a: La dirección es calle
   :answer_b: La dirección es 125 Main Street
   :answer_c: No se ejecutará
   :correct: a
   :feedback_a: Puesto que calle está entre comillas dobles imprimirá la cadena calle en lugar del valor de la variable calle.
   :feedback_b: Sería cierto si fuera print("La dirección es " + calle)
   :feedback_c: Aunque no imprime lo que probablemente desearíamos, imprimirá algo.

   Dado el siguiente fragmento de código, ¿qué se imprimirá?

   ::

     calle = "125 Main Street"
     print("La dirección es " + "calle")

.. mchoice:: 4_1_2_noSpace
   :answer_a: 125 Main Street, Atlanta, GA
   :answer_b: 125 Main Street,Atlanta, GA
   :answer_c: 125 Main Street Atlanta, GA
   :correct: b
   :feedback_a: Hubiera sido correcto si fuera calle + ", ".
   :feedback_b: No hay espacio después de la coma y no se añade de forma automática.
   :feedback_c: ¿Qué hay de la coma?

   ¿Qué se imprimirá cuando se ejecute lo siguiente?

   ::

     calle = "125 Main Street"
     ciudadEstado = "Atlanta, GA"
     print(calle + "," + cityState)

.. note::

    Discute los temas tratados en esta sección con tus compañeros.

      .. disqus::
          :shortname: uclm-eii-cs
          :identifier: studentcsp_4_1
