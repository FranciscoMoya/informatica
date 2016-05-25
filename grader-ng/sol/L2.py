# coding: utf-8

def suma_rango(a,b):
    return sum(range(a,b))

def contar_negativos(l):
    return len([x for x in l if x < 0])

def buscar_vocal(s):
    vocales = [ 'a','e','i','o','u',
                'A','E','I','O','U',
                'á','é','í','ó','ú',
                'Á','É','Í','Ó','Ú',
                'ü','Ü']
    pos = [ s.find(v) for v in vocales ]
    return min([ x for x in pos if x >= 0 ] or [-1])

def multiplos_7_en_rango(a, b):
    return len([ x for x in range(a,b) if x%7 == 0])

def dibujar_cuadrado(w):
    w -= 2
    print '+' + '-'*w + '+'
    for i in range(w/2):
        print '|' + ' '*w + '|'
    print '+' + '-'*w + '+'

from string import ascii_letters

def map(x):
    tr = dict(zip(ascii_letters, ascii_letters[3:] + ascii_letters[:3]))
    return tr[x] if x in tr else x

def codigo_cesar(s):
    return ''.join([map(x) for x in s])

def div(n):
    return [ x for x in range(1,n) if n % x == 0]

def es_perfecto(n):
    return n == sum(div(n))

def cifras(n):
    return [int(i) for i in str(n)]

def val(x):
    return x if x < 10 else .5

def puntuacion(a):
    v = sum([val(x) for x in a])
    return v if v <= 7.5 else 0.

def compara_bazas(a,b):
    va, vb = puntuacion(a), puntuacion(b)
    return 1 if va > vb else 2 if vb > va else 0

def buscar_texto(s, p):
    pos = [i for i in range(len(s)) if s[i:].startswith(p)]
    return len(pos)
