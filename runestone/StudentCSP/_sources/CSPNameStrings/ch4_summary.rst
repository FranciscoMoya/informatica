..  Copyright (C)  Mark Guzdial, Barbara Ericson, Briana Morrison
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3 or
    any later version published by the Free Software Foundation; with
    Invariant Sections being Forward, Prefaces, and Contributor List,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license
    is included in the section entitled "GNU Free Documentation License".

.. setup for automatic question numbering.

.. 	qnum::
	:start: 1
	:prefix: csp-4-5-


Capítulo 4 - Resumen
====================

El capítulo 4 incluye los siguientes conceptos de computación.

..	index::
        single: append
        single: capitalize
	single: concatenate
	single: function
	single: immutable
	single: index
	single: object
	single: string
	single: subcadena
        single: añadir
        single: capitalizar
	single: concatenar
	single: función
	single: inmutable
	single: índice
	single: objeto
	single: cadena
	single: subcadena

- **Añadir** - Puedes añadir una cadena a continuación de otra usando el símbolo ``+``.  También se le llama **concatenar**.
- **Capitalizar** - La función capitalize retorna una nueva cadena con el primer carácter en mayúscula.
- **Concatenar** - Puedes usar ``+`` para concatenar (añadir) dos cadenas así ``cadena3 = cadena1 + cadena2``.  Esto creará una nueva cadena llamada ``cadena3`` con todos los caracteres de la primera cadena ``cadena1``, seguidos por todos los caracteres de la segunda cadena, ``cadena2``.
- **Función** - Una función devuelve un valor.  Una función puede también recibir una entrada, aunque no tiene por qué.  Un ejemplo es la función de cadena ``lower()`` que devuelve una cadena con todos los caracteres en minúsculas.
- **Inmutable** - Inmutable significa que no cambia.  Las cadenas son inmutables en Python.  Cuando llames a una función que parece cambiar una cadena, realmente devolverá una nueva cadena.
- **Índice** - Un índice es un número asociado con la posición del carácter en la cadena.  En Python el primer carácter de una cadena está en el índice 0.
- **Objeto** - Un objeto puede tener comportamiento (cosas que puede hacer).  Por ejemplo, un objeto tortuga puede avanzar una cantidad determinada.  Las cadenas y las tortugas son objetos en Python.
- **Cadena** - Una cadena (string) es una secuancia de caracteres.  Se especifica como caracteres entre un par de comillas simples, dobles o triples.
- **Subcadena** -  Una subcadena es una parte de una cadena.  Una subcadena de "Hi there" sería "Hi".

Resumen de Funciones de Cadenas
-------------------------------

..	index::
	single: find
	single: len
	single: lower
	single: slice
	single: rodaja

El capítulo 4 también incluía las siguientes funciones de cadena.

- **append** - Se pueden sumar dos cadenas usando el símbolo ``+``.  También se llama **concatenar**.  El resultado de ``"Feliz" + " Cumpleaños"`` es ``"Feliz Cumpleaños"``.
- **find** - La función find de una cadena recibe una cadena como entrada y devuelve el **índice** de la primera ocurrencia de esa cadena en la cadena sobre la que se llama a la función.  El código ``"goodbye".find('bye')`` devuelve 4.
- **len** - La función len puede recibir una cadena como entrada y devuelve el número de caracteres de la cadena incluyendo los espacios.  Por ejemplo ``len("Hi there")`` devolverá 8.
- **lower** - La función lower de las cadenas devuelve una nueva cadena con solo letras minúscuas.  Por ejemplo  ``"ALL CAPS".lower()`` devuelve ``"all caps"``.
- **rodaja** - Puedes obtener parte de una cadena, también llamada **subcadena**, usando [comienzo] o [comienzo:final] que devolverá una subcadena de la cadena actual empezando en la posición de inicio indicada y, si se proporciona, hasta el carácter anterior a la posición final indicada.  Por ejemplo ``"salida"[1]`` devolverá ``"a"`` y ``"otter"[2:5]`` devuelve ``"ter"``.

.. note::

   Este es el final del capítulo 4.  Nos encantaría que nos dieras realimentación sobre este capítulo en https://www.surveymonkey.com/r/ch4-student-fb (en inglés).  Puede que te interese abrir este enlace en una nueva pestaña para facilitar la vuelta a este ebook.
