.. qnum::
   :prefix: 1-2-
   :start: 1

Test previo
-------------------------------------

A continuación realizaremos un test previo para comprobar lo que sabes acerca de la programación en Python.  No te preocupes si no entiendes las preguntas aún. No esperamos que lo hagas.  Simplemente contesta las preguntas a la medida de tus capacidades o elige "No lo se".

Las respuestas son almacenadas en el computador en el que estás trabajando para tu usuario.  Por tanto recomendamos iniciar sesión antes de empezar.  Inicia sesión pulsando sobre el busto de persona arriba a la izquierda en la ventana y selecciona login.  Pulsa en register si todavía no has creado tu usuario.

Pulsa sobre el botón "Start" cuando estés listo para empezar el examen.  Pulsa el botón "Pause" para parar temporalmente el examen (no podrás ver las preguntas mientras dure la pausa).  Mostrará cuánto tiempo has consumido, pero tienes tiempo ilimitado.  Pulsa en el botón "Finish Exam" al final cuando hayas acabado.  Los números de respuestas correctas, erróneas y no contestadas se mostrarán en la parte inferior de la página.  Para cada pregunta se mostrará también texto de realimentación además de tu propia respuesta.

No podrás cambiar las respuestas una vez que pulses el botón "Finish Exam".

.. timed:: preTest

    .. mchoice:: pre_1
       :answer_a: x = 7, y = 5, z = 0
       :answer_b: x = 5, y = 7, z = 7
       :answer_c: x = 5, y = 7, z = 0
       :answer_d: x = 5, y = 5, z = 7
       :answer_e: No lo se
       :correct: b
       :feedback_a: Esos son los valores originales, pero cambian.
       :feedback_b: x se pone a 7 pero cambia al valor de y que es 5.  y se pone a 5 originalmente, pero es cambiada al valor de z después de que z se ponga al valor de x que es 7. z se pone a 0 originalmente pero cambia al valor de x que es 7.
       :feedback_c: Sería cierta si al poner y como el valor de z se reseteare z a 0, pero no es eso lo que ocurre.
       :feedback_d: y se puso a 5 originalmente, pero el valor fue cambiado.
       :feedback_e: Vale, tranquilo.  No esperamos que lo sepas.

       ¿Cuáles serán los valores de x, y, z después de que se ejecuten las siguientes líneas de código?

       ::

          x = 7;
          y = 5;
          z = 0;
          z = x;
          x = y;
          y = z;


    .. mchoice:: pre_2
       :answer_a: Los mortales no pueden dividir por cero.
       :answer_b: 1000 / 4
       :answer_c: 250.0
       :answer_d: Los mortales no pueden dividir por cero. 250.
       :answer_e: No lo se
       :correct: c
       :feedback_a: La frase se imprime solo si denominador es igual a 0, pero no lo es.
       :feedback_b: Imprimirá el resultado de la división.
       :feedback_c: Imprime solamente el resultado de dividir 1000 por 4 que es 250.0.
       :feedback_d: La frase se imprime solo si denominador es igual a 0, pero no lo es.
       :feedback_e: Vale, tranquilo.  No esperamos que lo sepas.

       ¿Cuál es la salida del siguiente programa?

       ::

          denominador = 4
          if denominador == 0:
              print ("Los mortales no pueden dividir por cero.")
          else:
              print (1000 / denominador)

    .. mchoice:: pre_3
       :answer_a: Normal
       :answer_b: Crisis hipertensiva
       :answer_c: Presión sanguínea alta
       :answer_d: Prehipertensión
       :answer_e: No lo se
       :correct: c
       :feedback_a: Esto solo se imprimirá cuando tanto comprueba_sistolica como comprueba_diastolica devuelven 0, que es cuando a comprueba_sistolica se le pasa un número menor que 120 y a comprueba_diastolica se le pasa un número menor que 80.
       :feedback_b: Esto solo se imprimirá cuando comprueba_sistolica o bien comprueba_diastolica devuelve 3, que es cuando a comprueba_sistolica se le pasa un número mayor o igual a 180 y a comprueba_diastolica se le pasa un número mayor o igual a 110.
       :feedback_c: Esto se imprimirá cuando comprueba_sistolica sea 1 y comprueba_diastolica mayor que 1 (pero no 3).
       :feedback_d: Esto se imprimirá cuando comprueba_sistolica sea 1 y comprueba_diastolica menor o igual a 1.
       :feedback_e: Vale, tranquilo.  No esperamos que lo sepas.

       ¿Cuál es la salida del siguiente programa?

       ::

          def comprueba_sistolica(num1):
              if num1 < 120:
                  return 0
              elif num1 < 140:
                  return 1
              elif num1 < 180:
                  return 2
              else:
                  return 3

          def comprueba_diastolica(num2):
              if num2 < 80:
                  return 0
              elif num2 < 90:
                  return 1
              elif num2 < 110:
                  return 2
              else:
                  return 3

          sistolica = 135
          diastolica = 100
          if   comprueba_sistolica(sistolica) == 0 and \
               comprueba_diastolica(diastolica) == 0:
              print ("Normal")
          elif comprueba_sistolica(sistolica) == 3 or \
               comprueba_diastolica(diastolica) == 3:
              print ("Crisis hipertensiva")
          elif comprueba_sistolica(sistolica) == 1:
              if comprueba_diastolica(diastolica) > 1:
                  print ("Presión sanguínea alta")
              else:
                  print ("Prehipertensión")


    .. mchoice:: pre_4
       :answer_a: 10         [3, 1, -2]         -1
       :answer_b:  6         [3, 1, -2]          2
       :answer_c:  6         [3, 1, -2]         -1
       :answer_d:  6         [3, 1, -2]         -2
       :answer_e: No lo se
       :correct: c
       :feedback_a: Esto imprimiria 10 al principio si las listas empezaran en el índice 1, pero empiezan en índice 0.
       :feedback_b: Recuerda que las listas empiezan en índice 0.
       :feedback_c: Las listas empiezan en índice 0.  Puedes modificar el valor en un índice dado.
       :feedback_d: Date cuenta de que segunda[2] es incrementado.
       :feedback_e: Vale, tranquilo.  No esperamos que lo sepas.

       ¿Cuál es la salida del siguiente programa?

       ::

          primera = [10,5,10,6]
          print (primera[3])
          segunda = [3,1,-2]
          print (segunda)
          segunda[2] = segunda[2] + 1
          print (segunda[2])

    .. mchoice:: pre_5
       :answer_a: [-5, 5, 0]  [3, 1, 3, 5]
       :answer_b: [10, 5, 0]  [3, 1, 3, 100]
       :answer_c: [10, -5, 0]  [3, 1, 3, 5]
       :answer_d: [10, -5, 0]  [3, 1, 3, 100]
       :answer_e: No lo se
       :correct: d
       :feedback_a: El primer valor en primera no cambia. primera[1] se refiere al segundo elemento de la lista.
       :feedback_b: El segundo elemento (el que está en el índice 1) en la lista primera se cambia a -5.
       :feedback_c: El último elemento de la lista segunda se cambia a 100.
       :feedback_d: El segundo elemento (el que está en el índice 1) en la lista primera se cambia a -5. El último elemento de la lista segunda se cambia a 100.
       :feedback_e: Vale, tranquilo.  No esperamos que lo sepas.

       ¿Cuál es la salida del siguiente programa?

       ::

          primera = [10,5,0]
          primera[1] = -5
          valor = primera[2]
          print (primera)
          segunda = [3,1,3,valor]
          segunda[3] = 100
          print (segunda)

    .. mchoice:: pre_6
       :answer_a: Imprimirá "Hola Roger"
       :answer_b: Imprimirá "Hola nombre"
       :answer_c: Imprimirá "Adiós Roger"
       :answer_d: Imprimirá hola + " " + nombre
       :answer_e: No lo se
       :correct: c
       :feedback_a: Imprimirá el valor de hola, que es "Adiós".
       :feedback_b: Imprimirá el valor de hola, que es "Adiós".
       :feedback_c: Imprimirá el valor de hola, que es "Adiós" y el valor de nombre, que es "Roger" con un espacio en medio.
       :feedback_d: Imprime los valores de las variables.
       :feedback_e: Vale, tranquilo.  No esperamos que lo sepas.

       Given the following code segment, which of the following statements is true?

       ::

          hola = "Adiós"
          roger = "nombre"
          nombre = "Roger"
          saludo = hola+" "+nombre
          print (saludo)

    .. mchoice:: pre_7
       :answer_a: El resultado imprimido será par y tendrá punto decimal.
       :answer_b: El resultado imprimido será impar y tendrá punto decimal.
       :answer_c: El resultado imprimido será par y no tendrá punto decimal.
       :answer_d: El resultado imprimido será impar y no tendrá punto decimal.
       :answer_e: No lo se
       :correct: c
       :feedback_a: Sumar un número par de números pares resulta en una suma par, pero no habrá punto decimal.
       :feedback_b: Sumar un número par de números pares resulta en una suma par.
       :feedback_c: Sumar un número par de números pares resulta en una suma par y no habrá punto decimal.
       :feedback_d: Sumar un número par de números pares resulta en una suma par.
       :feedback_e: Vale, tranquilo.  No esperamos que lo sepas.

       Dado el siguiente fragmento de código, ¿cuál de las siguientes opciones es cierta?

       ::

          sum = 0 # Empieza sin nada
          cosasParaSumar = [1,3,7,19,21,131]
          for number in cosasParaSumar:
              sum = sum + number
          print (sum)

    .. mchoice:: pre_8
       :answer_a: El resultado imprimido será par y tendrá punto decimal.
       :answer_b: El resultado imprimido será impar y tendrá punto decimal.
       :answer_c: El resultado imprimido será par y no tendrá punto decimal.
       :answer_d: El resultado imprimido será impar y no tendrá punto decimal.
       :answer_e: No lo se
       :correct: d
       :feedback_a: Sumar un número impar de números impares resulta en una suma impar.
       :feedback_b: Hubiera sido correcta si alguno de los números tuviera punto decimal.
       :feedback_c: Sumar un número impar de números impares resulta en una suma impar.
       :feedback_d: Puesto que ninguno de los números tiene punto decimal la respuesta tampoco lo tendrá.
       :feedback_e: Vale, tranquilo.  No esperamos que lo sepas.

       Dado el siguiente fragmento de código, ¿cuál de las siguientes opciones es cierta?

       ::

          counter = 1
          sum = 0
          while counter <= 10:
              sum = sum + counter
              counter = counter + 2
          print (sum)



    .. mchoice:: pre_9
       :answer_a: El resultado imprimido solo contendrá vocales.
       :answer_b: El resultado imprimido solo contendrá consonantes.
       :answer_c: Imprimirá la cadena vacía.
       :answer_d: El resultado imprimido incluirá "y"
       :answer_e: No lo se
       :correct: a
       :feedback_a: Solo añade la letra si es una vocal.
       :feedback_b: Solo añade la letra si es una vocal.
       :feedback_c: No, añadirá vocales a nuevaCadena e la imprimirá.
       :feedback_d: La letra debe estar en "aeiou" para ser añadida a nuevaCadena.
       :feedback_e: Vale, tranquilo.  No esperamos que lo sepas.

       Dado el siguiente fragmento de código, ¿cuál de las siguientes frases es cierta?

       ::

          nuevaCadena = ""
          frase = "Dime cuantos cuentos cuentas cuando cuentas cuentos."
          for letra in frase:
              if letra in "aeiou":
                  nuevaCadena = nuevaCadena + letra
          print (nuevaCadena)

    .. mchoice:: pre_10
       :answer_a: La tortuga en este ejemplo dibuja un pentagrama.
       :answer_b: La tortuga dibuja cuatro líneas de longitudes 5, 11, 16, y 21.
       :answer_c: La tortuga dibuja un cuadrado.
       :answer_d: Este código generará un error.
       :answer_e: No lo se
       :correct: c
       :feedback_a: Itera 4 veces, ¿cómo va a ser un pentagrama?
       :feedback_b: Siempre se mueve hacia adelante 100 unidades.
       :feedback_c: Dibuja un cuadrado con lados de longitud 100.
       :feedback_d: No se generará ningún error.
       :feedback_e: Vale, tranquilo.  No esperamos que lo sepas.

       Dado el siguiente fragmento de código, ¿cuál de las siguientes frases es cierta?

       ::

          from turtle import *
          espacio = Screen()
          alicia = Turtle()
          alicia.setheading(90)
          for lados in [5,11,16,21]:
              alicia.forward(100)
              alicia.right(90)

    .. mchoice:: pre_11
       :answer_a: 29
       :answer_b: 182
       :answer_c: 153
       :answer_d: 181
       :answer_e: No lo se
       :correct: c
       :feedback_a: Suma los elementos de índices impares en la lista (empezando en el de índice 1 que ocupa el segundo lugar de la lista).
       :feedback_b: Suma los elementos de índices impares en la lista (empezando en el de índice 1 que ocupa el segundo lugar de la lista).
       :feedback_c: Suma los elementos de índices impares en la lista (empezando en el de índice 1 que ocupa el segundo lugar de la lista).
       :feedback_d: Suma los elementos de índices impares en la lista (empezando en el de índice 1 que ocupa el segundo lugar de la lista).
       :feedback_e: Vale, tranquilo.  No esperamos que lo sepas.

       Dado el siguiente fragmento de código, ¿qué se imprimirá en pantalla?

       ::

          sum = 0 # Empieza sin nada
          cosasParaSumar = [1,3,7,19,21,131]
          for numero in range(1,len(cosasParaSumar),2):
              sum = sum + cosasParaSumar[numero]
          print(sum)
