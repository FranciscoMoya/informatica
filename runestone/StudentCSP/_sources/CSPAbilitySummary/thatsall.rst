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
	:prefix: csp-19-1-


Capacidades del Computador
================================================

¿Realmente es eso todo lo que un computador puede hacer? ¿nombrar cosas, repetir pasos, tomar decisiones, y manipular datos?

Si, así es -- eso es todo.  Todo lo demás que puede hacer un computador son combinaciones de esas capacidades:

- Nombrar valores, transferirlos de un lado a otro, y hacer cálculos aritméticos sobre ellos.

- Nombrar cualquier cosa, incluyendo nombres para pasos, nombres para nombres.

- Repetir instrucciones.

- Comprobar cosas (usar condicionales) y hacer algo según el resultado.

- Acceder a partes de una colección de datos.

.. index::
  single: abstraction
  single: abstracción

Esto es suficiente para construir una Máquina de Turing.  De hecho, cualquier cosa que pueda ser susceptible de ser computada, puede computarse con solo estas cuatro capacidades, combinadas de de formas diferentes y a veces sorprendentes.  Probablemente la forma más poderosa es la llamada **abstracción**.  Un ejemplo de **abstracción** es cuando creas una función o procedimiento.  Otros pueden usar esa función o procedimiento sin saber o preocuparse de ningún detalle acerca de cómo funciona.

Si piensas en lo que tú sabes que la gente hace con un ordenador, la afirmación de que estas cuatro capacidades son todo lo que necesitas para hacer *todo* puede parecer traída por los pelos.  ¿Cómo se comunica un ordenador con un ser humano o con otro computador?  Todas las conexiones al mundo exterior del ordenador aparecen como memoria (valores de variable especiales) para el ordenador.

- *"¿Qué hay de leer de un teclado o de un ratón?"* Los teclados o los ratones se conectan al ordenador como si se tratara de una localización de memoria especial.  Piensa en una variable llamada ``ultimaTeclaPulsada`` que devolviera un carácter que es la última tecla pulsada en el teclado, o ``posicionRaton`` que muestra dónde debería estar el cursor del ratón ahora.  El computador podría ejecutar un bucle, comprobando si hay nuevas teclas pulsadas o nuevas posiciones del ratón, y actualizando la pantalla de acuerdo a ésto.

- *"¿Y qué hay de los gráficos?"*  Cambiar la pantalla es simplemente cambiar memoria (variables).  Puedes pensar en la pantalla como un puñado de You can think about the display as a much of little dotspequeños puntos (pixels) dispuestos a lo largo de un eje horizontal y otro vertical.  Cada punto tiene tres partes en él -- una parte roja, una parte verde y una parte azul.  Encender el rojo al máximo en el punto que está a 100 puntos del borde izquierdo en sentido horizontal y a 200 puntos del borde superior en sentido vertical puede entenderse como ``display[100][200].red = 255``.

- *"¿Y qué hay de los robots?  He encendido un motor de un robot, y he leído datos de un sensor del robot."*  De nuevo se trata de memoria.  Podemos pensar en una localización especial de memoria que controla el motor, ``robotMotor = 0`` podría apagarlo, y ``robotMotor = 1`` podría encenderlo.  Los datos de sensores podrían estar disponibles como un número leído de una variable especial, e.g., ``tocandoParachoques = leerRobotSensorPresion``.

Ahora piensa en todas las maravillosas cosas que hacen los computadores, desde las búsquedas en miles de millones de sitios web, hasta el análisis masivo de datos para el seguimiento de estrellas, o la compartición de mensajes entre millones de amigos en línea.  *Todas* estas pueden entenderse en términos de estas cuatro capacidades.

Los computadores son rápidos.  Un computador típico podría ejecutar una sentencia de asignación en una *billonésima* de segundo.  Es incluso difícil escribir un programa que tarde más de un segundo en ejecutarse.  La mayoría de lo que hacen los computadores hoy en día es *esperar* -- esperar a que los datos vengan de la red (que el computador ve, como habrás adivinado, como otra localización de memoria), o esperar al usuario a que pulse una tecla o mueva el ratón.

.. index::
  single: Halting Problem
  single: Problema de la parada

Sabemos que hay límites en lo que podemos computar.  Por ejemplo, sabemos que no podemos escribir un programa que compruebe todos los demás programas.  El problema se conoce como el *Problema de la Parada* (*Halting Problem*).  Imagina un programa como una gran cadena de caracteres.  Sabemos que podemos buscar partes de esa cadena utilizando indexación.  Sabemos que podemos tomar decisiones usando sentencias ``if``.  ¿Podemos escribir un programa que lee otros programas como cadenas, y nos dice si funcionará o no?  Alan Turing, el mismo brillante matemático que definió los computadores, también escribió una prueba matemática de que tal programa es *impossible*.  No podemos escribir un "comprobador de programas" general.

Pero desconocemos los límites de la computación con respecto a nosotros mismos.  ¿Somos computables? ¿Es nuestra inteligencia simplemente un programa grande y complicado, con millones de condiciones, centenares de bucles y billones de variables? ¿Es posible escribir un programa que *sea* inteligente?  No sabemos aún las respuestas a estas preguntas, pero es un problema fascinante ver hasta dónde podemos llevar la máquina de Alan Turing.
