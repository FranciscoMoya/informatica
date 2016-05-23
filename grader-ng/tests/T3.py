import unittest, sys

from L3 import \
    comunidades_autonomas, \
    aprobados_pau, \
    suspensos_pau, \
    comunidad_mas_aprobados, \
    comunidad_mas_diferencia    

csv = 'tests/pcaxis637310428.csv'

class Test_3(unittest.TestCase):
    
    def test_comunidades_autonomas(self):
        self.assertEqual([], comunidades_autonomas(csv))

    
    def test_aprobados_pau(self):
        pass

    
    def test_suspensos_pau(self):
        pass

    
    def test_comunidad_mas_aprobados(self):
        pass

    
    def test_comunidad_mas_diferencia(self):
        pass



