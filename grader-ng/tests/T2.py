import unittest, sys

try: from L2 import suma_rango
except: pass

try: from L2 import contar_negativos
except: pass

try: from L2 import buscar_vocal
except: pass

try: from L2 import multiplos_7_en_rango
except: pass

try: from L2 import dibujar_cuadrado
except: pass

try: from L2 import codigo_cesar
except: pass

try: from L2 import es_perfecto
except: pass

try: from L2 import cifras
except: pass

try: from L2 import compara_bazas
except: pass

try: from L2 import buscar_texto
except: pass


class Test_2(unittest.TestCase):

    def setUp(self):
        self.console = sys.stdout
        sys.stdout = open('/tmp/out.txt', 'w')

    def tearDown(self):
        sys.stdout = self.console

    def test_suma_rango(self):
        self.assertEqual(suma_rango(5,5), 0)
        self.assertEqual(suma_rango(0,5), 10)
        self.assertEqual(suma_rango(5,10), 35)
        self.assertEqual(suma_rango(-3,4), 0)
    
    def test_contar_negativos(self):
        self.assertEqual(contar_negativos([]), 0)
        self.assertEqual(contar_negativos([0, -2, 0, -1]), 2)
        self.assertEqual(contar_negativos([0, -1, -1]), 2)
        self.assertEqual(contar_negativos([0, 1, 1]), 0)
    
    def test_buscar_vocal(self):
        self.assertEqual(buscar_vocal('prueba'), 2)
        self.assertEqual(buscar_vocal('PRUEBA'), 2)
        self.assertEqual(buscar_vocal('AEIOU'), 0)
        self.assertEqual(buscar_vocal('Sdzqrt3'), -1)
        self.assertEqual(buscar_vocal('prJ3b4 s1n V0C4L3S'), -1)
    
    def test_multiplos_7_en_rango(self):
        self.assertEqual(multiplos_7_en_rango(1,7), 0)
        self.assertEqual(multiplos_7_en_rango(1,14), 1)
        self.assertEqual(multiplos_7_en_rango(7,21), 2)
        self.assertEqual(multiplos_7_en_rango(7,77), 10)
    
    def test_dibujar_cuadrado(self):
        self.assertEqual(self.std_output(dibujar_cuadrado(12)),
                         ['+----------+',
                          '|          |',
                          '|          |',
                          '|          |',
                          '|          |',
                          '|          |',
                          '+----------+'])
        self.clear_std_output()
        self.assertEqual(self.std_output(dibujar_cuadrado(8)),
                         ['+------+',
                          '|      |',
                          '|      |',
                          '|      |',
                          '+------+'])
        self.clear_std_output()
        self.assertEqual(self.std_output(dibujar_cuadrado(4)),
                         ['+--+',
                          '|  |',
                          '+--+'])
        self.clear_std_output()
        self.assertEqual(self.std_output(dibujar_cuadrado(2)),
                         ['++',
                          '++'])

    def test_codigo_cesar(self):
        self.assertEqual(codigo_cesar('abcdef'), 'defghi')
        self.assertEqual(codigo_cesar('ABCDEF'), 'DEFGHI')
        self.assertEqual(codigo_cesar('MaximoSecreto'), 'PdAlprVhfuhwr')
    
    def test_es_perfecto(self):
        self.assertTrue(es_perfecto(6))
        self.assertTrue(es_perfecto(28))
        self.assertTrue(es_perfecto(496))
        self.assertTrue(es_perfecto(8128))
        self.assertFalse(es_perfecto(5))
        self.assertFalse(es_perfecto(27))
        self.assertFalse(es_perfecto(495))
        self.assertFalse(es_perfecto(8127))
    
    def test_cifras(self):
        self.assertEqual(cifras(2016), [2,0,1,6])
        self.assertEqual(cifras(123456789), range(1,10))
        self.assertEqual(cifras(9876543210), range(9,-1,-1))
    
    def test_compara_bazas(self):
        self.assertEqual(compara_bazas([1,5,12], [7,10]), 2)
        self.assertEqual(compara_bazas([2,5,12], [7,10]), 0)
        self.assertEqual(compara_bazas([5,12], [3,10]), 1)
        self.assertEqual(compara_bazas([5,12,3], [5,10]), 2)
        self.assertEqual(compara_bazas([5,12,3], [5,10,4]), 0)
    
    def test_buscar_texto(self):
        self.assertEqual(buscar_texto('No por mucho madrugar amanece mas temrano', 'ma'), 3)
        self.assertEqual(buscar_texto('No aparece el texto', 'pares'), 0)
        self.assertEqual(buscar_texto('Aparece el texto', 'pare'), 1)
        self.assertEqual(buscar_texto('reparepare', 'repare'), 2)

    def std_output(self, _):
        sys.stdout.flush()
        with open('/tmp/out.txt', 'r') as f:
            return [x.strip() for x in f.readlines()]
        
    def clear_std_output(self):
        sys.stdout.truncate(0)
        sys.stdout.seek(0)
        
