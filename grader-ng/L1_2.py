def recortar(x):
    if x > 1.0:
        return 1.0
    if x < -1.0:
        return -1.0
    return x


def es_bisiesto(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


def es_primo(n):
    if not n > 1:
        return False
    
    for i in range(2,n//2):
        if n % i == 0:
            return False

    return True


from math import sqrt

def media_geometrica(x, y):
    return sqrt(x*y)


def bateria_cargada(x):
    if 12.5 <= x <= 12.95:
        return True
    if -12.95 <= x <= -12.5:
        return True
    return False


def calificacion(x):
    if x < 5.:
        return 'Suspenso'
    if 5. <= x < 7.:
        return 'Aprobado'
    if 7. <= x < 9.:
        return 'Notable'
    return 'Sobresaliente'


def fahrenheit_a_celsius(f):
    return (f - 32.) / 1.8


from math import pi

def area_circulo(r):
    return pi*r**2


def v(t):
    return 9.8*t

def energia_cinetica(m,t):
    return .5*m*v(t)**2
 

def redondear(x):
    return int(round(x))
 
