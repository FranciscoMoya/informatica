import unittest

from L1_1 import my_email
from L1_2 import \
    recortar, \
    es_bisiesto, \
    es_primo, \
    media_geometrica, \
    bateria_cargada, \
    calificacion, \
    fahrenheit_a_celsius, \
    area_circulo, \
    energia_cinetica, \
    redondear

from math import pi
epsilon = 0.001



class Test_1_1(unittest.TestCase):
    
    def test_my_email(self):
        self.assertEqual(1, my_email().count('@'))
        self.assertTrue(my_email().endswith('uclm.es'))



class Test_1_2(unittest.TestCase):

    def test_recortar(self):
        self.assertEqual(recortar(120), 1.0)
        self.assertEqual(recortar(-120), -1.0)
        self.assertEqual(recortar(0.75), 0.75)
        self.assertEqual(recortar(-0.25), -0.25)

    def test_es_bisiesto(self):
        self.assertTrue(es_bisiesto(4))
        self.assertFalse(es_bisiesto(100))
        self.assertTrue(es_bisiesto(400))
        self.assertTrue(es_bisiesto(2000))
        self.assertFalse(es_bisiesto(1900))
        self.assertTrue(es_bisiesto(2016))
        
    def test_es_primo(self):
        self.assertFalse(es_primo(0))
        self.assertFalse(es_primo(1))
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(17))
        self.assertFalse(es_primo(18))
        self.assertTrue(es_primo(19))
        self.assertTrue(es_primo(97))
        self.assertFalse(es_primo(98))
        self.assertFalse(es_primo(99))

    def test_media_geometrica(self):
        self.assertEqual(media_geometrica(1.0, 1.0), 1.0)
        self.assertEqual(media_geometrica(4.0, 25.0), 10.0)
        self.assertEqual(media_geometrica(100.0, 16.0), 40.0)
        self.assertEqual(media_geometrica(2.0, 1.125), 1.5)

    def test_bateria_cargada(self):
        self.assertTrue(bateria_cargada(12.5))
        self.assertTrue(bateria_cargada(12.95))
        self.assertTrue(bateria_cargada(12.75))
        self.assertFalse(bateria_cargada(12.96))
        self.assertFalse(bateria_cargada(12.49))
        self.assertTrue(bateria_cargada(-12.5))
        self.assertTrue(bateria_cargada(-12.95))
        self.assertTrue(bateria_cargada(-12.75))
        self.assertFalse(bateria_cargada(-12.96))
        self.assertFalse(bateria_cargada(-12.49))

    def test_calificacion(self):
        self.assertEqual(calificacion(4.9), 'Suspenso')
        self.assertEqual(calificacion(5.0), 'Aprobado')
        self.assertEqual(calificacion(6.9), 'Aprobado')
        self.assertEqual(calificacion(7.0), 'Notable')
        self.assertEqual(calificacion(8.9), 'Notable')
        self.assertEqual(calificacion(9.0), 'Sobresaliente')
        self.assertEqual(calificacion(10.0), 'Sobresaliente')
    
    def test_fahrenheit_a_celsius(self):
        self.assertEqual(fahrenheit_a_celsius(32.0), 0.0)
        self.assertEqual(fahrenheit_a_celsius(86.0), 30.0)
        self.assertEqual(fahrenheit_a_celsius(212.0), 100.0)
    
    def test_area_circulo(self):
        self.assertTrue(abs(area_circulo(1.0) - pi) < epsilon)
        self.assertTrue(abs(area_circulo(2.0) - 4.*pi) < epsilon)
        self.assertTrue(abs(area_circulo(1.25) - 1.5625*pi) < epsilon)
        self.assertTrue(area_circulo(0) == 0.0)
    
    def test_energia_cinetica(self):
        self.assertTrue(abs(energia_cinetica(1,2) - 192.08) < epsilon)
        self.assertTrue(abs(energia_cinetica(2,1) - 96.04) < epsilon)
        self.assertTrue(abs(energia_cinetica(2,2) - 384.16) < epsilon)
        self.assertTrue(abs(energia_cinetica(1,4) - 768.32) < epsilon)
    
    def test_redondear(self):
        self.assertIs(type(redondear(1.25)), int)
        self.assertEqual(redondear(1.0), 1)
        self.assertEqual(redondear(1.25), 1)
        self.assertEqual(redondear(1.25), 1)
        self.assertEqual(redondear(1.55), 2)
        self.assertEqual(redondear(1.5), 2)
