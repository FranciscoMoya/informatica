.. qnum::
   :prefix: 4-7-
   :start: 1

Preguntas de Examen para los capítulos 3 y 4
--------------------------------------------

Las siguientes preguntas comprueban lo que has aprendido en los capítulos 3 y 4.  Pulsa sobre el botón "Start" cuando estés listo para empezar el examen.  Pulsa el botón "Pause" para parar temporalmente el examen (no podrás ver las preguntas mientras dure la pausa).  Mostrará cuánto tiempo has consumido, pero tienes tiempo ilimitado.  Pulsa en el botón "Finish Exam" al final cuando hayas acabado.  Los números de respuestas correctas, erróneas y no contestadas se mostrarán en la parte inferior de la página.  Para cada pregunta se mostrará también texto de realimentación además de tu propia respuesta.

No podrás cambiar las respuestas una vez que pulses el botón "Finish Exam".

.. timed:: ch3a4ex

    .. mchoice:: e3a4_1
       :answer_a: nombrepalabras
       :answer_b: nombre + palabras
       :answer_c: John Smith + disfruta jugando fuera.
       :answer_d: John Smith disfruta jugando fuera.
       :correct: d
       :feedback_a: Sería cierto si fuera print ("nombre" + "palabras"), pero nombre y palabras no están entre comillas por lo que se imprimirá el valor de cada una.
       :feedback_b: Sería cierto si fuera print ("nombre + palabras").
       :feedback_c: Sería cierto si fuera print (nombre + " +" + palabras).
       :feedback_d: Cuando usas un nombre de variable en una sentencia print se imprime el valor de la variable.  El signo + se usa para unir dos cadenas.

       ¿Qué se imprime cuando se ejecuta el código siguiente?

       ::

          nombre = "John Smith"
          palabras = " disfruta jugando fuera."
          print (nombre + palabras)

    .. mchoice:: e3a4_2
       :answer_a: Comprueba si los valores a cada lado de la expresión son iguales
       :answer_b: Asigna el nombre a la izquierda al valor de la derecha
       :answer_c: Copia el valor de la derecha a la izquierda
       :answer_d: Crea dos objetos nuevos, uno llamado gato y otro llamado miau
       :correct: b
       :feedback_a: Sería cierto si fuera gato == "miau".
       :feedback_b: Un nombre a la la izquierda y un valor a la derecha crea una variable con ese nombre y ese valor.
       :feedback_c: Sería cierto si fuera un nombre de variable en la derecha en lugar de una cadena.
       :feedback_d: Crea una variable y ajusta su valor.  No crea un objeto.

       En el código siguiente, ¿qué hace el "="?

       ::

          gato = "miau"

    .. mchoice:: e3a4_3
       :answer_a: I solamente
       :answer_b: II solamente
       :answer_c: III solamente
       :answer_d: Todos ellos
       :correct: b
       :feedback_a: No hay comillas alrededor de la cadena, por lo que dará un error.
       :feedback_b: Cuando usas '+' añade las cadenas una a continuación de otra, por lo que imprimirá la cadena correcta.
       :feedback_c: La respuesta III no funcionará puesto que no hay ninguna variable llamada Morrissey.
       :feedback_d: La respuesta II funcionará, pero no lo hará la I o la III.  La respuesta I no tiene comillas alrededor de la cadena.  En  III no hay variable llamada Morrissey.

       ¿Cuál de los siguientes grupos de líneas de código imprimirá "Mi nombre es Morrissey"?

       ::

          I.   print (Mi nombre es Morrissey)
          II.  var1 = "Mi nombre es "
               var2 = "Morrissey"
               var3 = var1 + var2
               print (var3)
          III. M = "M"
               orrissey = "orrissey"
               print ("Mi nombre es " + Morrissey)

    .. mchoice:: e3a4_4
       :answer_a: 0
       :answer_b: 2
       :answer_c: 5
       :answer_d: 1
       :correct: d
       :feedback_a: Sería cierto si fuera 4 % 2 puesto que 2 cabe exactamente 2 veces en 4.
       :feedback_b: Sería cierto si fuera 5 % 3.
       :feedback_c: Sería cierto si dividieras 5 por un número mayor que 5.
       :feedback_d: 2 cabe en 5 2 veces con un resto de 1.

       ¿Qué se imprime después de ejecutar lo siguiente?

       ::

          resultado = 5 % 2
          print(resultado)

    .. mchoice:: e3a4_5
       :answer_a: 3
       :answer_b: 10
       :answer_c: 18
       :answer_d: 0
       :correct: b
       :feedback_a: Aunque var2 empieza con el valor 3 cambia se ajusta a una copia del valor en var1.
       :feedback_b: Aunque var2 empieza con el valor 3 cambia se ajusta a una copia del valor en var1, que es 10.
       :feedback_c: Este es el valor de var1 después de que se ejecute el código.
       :feedback_d: Tendrías que haber ajustado var2 al valor 0 en algún punto para que fuera cierto.

       ¿Cuál es el valor de var2 después de que se ejecute el siguiente código?

       ::

          var2 = 3
          var1 = 10
          var2 = var1
          var3 = var2
          var1 = 18

    .. mchoice:: e3a4_6
       :answer_a: THIS IS A TEST
       :answer_b: this is a test
       :answer_c: This is a test
       :answer_d: This is a test, really!
       :correct: a
       :feedback_a: Strings are immutable.  Any change to a string returns a new string.
       :feedback_b: Sería cierto si the question asked for the value of better.
       :feedback_c: Sería cierto si the question asked for the value of betterStill
       :feedback_d: Sería cierto si the question asked for the value of more.

       ¿Cuál es el valor de frase después de ejecutar el siguiente código?

       ::

          frase = "ESTO ES UNA PRUEBA"
          mejor = frase.lower()
          print(mejor)
          aunMejor = aunMejor.capitalize() + "."
          mas = frase + ", ¡ en serio!"
