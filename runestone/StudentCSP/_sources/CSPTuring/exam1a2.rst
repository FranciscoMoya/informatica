.. qnum::
   :prefix: 2-5-
   :start: 1

Preguntas de Examen para los Capitulos 1 y 2
--------------------------------------------

Las siguientes preguntas comprueban lo que has aprendido en los capítulos 1 y 2.  Pulsa sobre el botón "Start" cuando estés listo para empezar el examen.  Pulsa el botón "Pause" para parar temporalmente el examen (no podrás ver las preguntas mientras dure la pausa).  Mostrará cuánto tiempo has consumido, pero tienes tiempo ilimitado.  Pulsa en el botón "Finish Exam" al final cuando hayas acabado.  Los números de respuestas correctas, erróneas y no contestadas se mostrarán en la parte inferior de la página.  Para cada pregunta se mostrará también texto de realimentación además de tu propia respuesta.

No podrás cambiar las respuestas una vez que pulses el botón "Finish Exam".

.. timed:: ch1a2ex

    .. mchoice:: e1a2_1
       :answer_a: perro
       :answer_b: pez
       :answer_c: gato
       :answer_d: pájaro
       :correct: a
       :feedback_a: El valor de var3 es inicilamente "pájaro" pero después cambió al valor de var1.  El valor de var1 es inicialmente "gato" pero luego cambió al valor de var2 que tenía "perro".
       :feedback_b: Solo var2 tiene el valor pez.  Cuando asignas el valor de una variable a otra variable el valor es copiado a la nueva variable.  No se crea ninguna relación entre las dos variables.
       :feedback_c: El valor de var3 es inicialmente "pájaro" pero después cambió al valor de var1. Sin embargo el valor de var1 también cambión después de la asociación original.
       :feedback_d: Aunque el valor de var3 es originalmente "bird", éste es cambiado posteriormente.

       ¿Cuál es el valor de var3 después de ejecutar el código siguiente?

       ::

          var1 = "gato"
          var2 = "perro"
          var3 = "pájaro"
          var1 = var2
          var3 = var1
          var2 = "pez"

    .. mchoice:: e1a2_2
       :answer_a: variable
       :answer_b: tortuga
       :answer_c: cadena (string)
       :answer_d: programa
       :correct: a
       :feedback_a: Una variable es un nombre asociado con un espacio (memoria del computador) que contiene un valor. Ese valor puede cambiar o variar.
       :feedback_b: Una tortuga es un objeto que puede avanzar y girar.  Conforme se mueve puede dibujar el camino.
       :feedback_c: Una cadena es una secuencia de caracteres.
       :feedback_d: Un programa es un conjunto de instrucciones que un computador puede ejecutar.

       ¿Cuál de las siguientes corresponde a un espacio con nombre que puede contener un valor?

    .. mchoice:: e1a2_3
       :answer_a: entero
       :answer_b: tortuga
       :answer_c: cadena
       :answer_d: imagen
       :correct: c
       :feedback_a: Un entero es un número positivo o negativo sin decimales.
       :feedback_b: Una tortuga es un objeto que puede avanzar y girar.  Conforme se mueve puede dibujar el camino.
       :feedback_c: Una cadena es una secuencia de caracteres.
       :feedback_d: Una imagen es una representación de una fotografía digital y puedes obtener y cambiar los colores de cada pixel de la imagen.

       ¿Cuál de las siguientes corresponde a la clase de datos que puede contener letras, dígitos y otros caracteres entre comillas simples o dobles?

    .. mchoice:: e1a2_4
       :answer_a: 3
       :answer_b: 2
       :answer_c: 5
       :answer_d: 0
       :correct: b
       :feedback_a: Ese es el valor original de var1. ¿Cuál es el valor de var2?
       :feedback_b: Cuando a var1 se le asigna elvalor de var2 el valor de var2 es copiado y no cambiado.
       :feedback_c: Ese es el valor original de var3. ¿Cuál es el valor de var2?
       :feedback_d: Cuando a una variable (var1) se le asigna el valor de otra (var2) copia el valor de la otra (var2).  No cambia el valor en la otra (var2).

       ¿Cuál es el valor de var2 después de ejecutar el siguiente código?

       ::

          var1 = 3
          var2 = 2
          var3 = 5
          var1 = var2

    .. mchoice:: e1a2_5
       :answer_a: Un cuadrado
       :answer_b: Un rectángulo que es mas alto que ancho
       :answer_c: Un rombo
       :answer_d: Un rectángulo que es mas ancho que alto
       :correct: b
       :feedback_a: Sería cierto si todos los avances fueran de la misma cantidad.
       :feedback_b: La cabeza de Zari se orienta a 90 que corresponde al norte.  Por tanto el rectángulo es más alto que ancho.
       :feedback_c: Sería cierto si todos los avances fueran de la misma cantidad y empezara con orientación 45.
       :feedback_d: Las tortugas empiezan mirando al este y poner la orientación a 90 la gira mirando al norte.

       ¿Que figura dibujará el siguiente código?

       ::

         from turtle import *        # usar la biblioteca turtle
         space = Screen()            # crear una espacio de tortugas (space)
         zari = Turtle()             # crear una tortuga llamada zari
         zari.setheading(90)
         zari.forward(100)           # avanzar zari en 100 unidades
         zari.right(90)              # girar 90 grados
         zari.forward(50)            # avanzar zari en 100 unidades
         zari.right(90)              # girar 90 grados
         zari.forward(100)           # avanzar zari en 100 unidades
         zari.right(90)              # girar 90 grados
         zari.forward(50)            # avanzar zari en 100 unidades
         zari.right(90)              # girar 90 grados
