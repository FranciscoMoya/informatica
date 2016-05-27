import unittest, sys

try: from lab import comunidades_autonomas
except: pass

try: from lab import aprobados_pau
except: pass

try: from lab import suspensos_pau
except: pass

try: from lab import comunidad_mas_aprobados
except: pass

try: from lab import comunidad_mas_diferencia
except: pass

csv = 'tests/pcaxis637310428.csv'

class Test_3(unittest.TestCase):
    
    def test_comunidades_autonomas(self):
        ca = sorted(comunidades_autonomas(csv))
        self.assertEqual(ca[0], 'A distancia')
        self.assertEqual(ca[3], 'Asturias; Principado de')
        self.assertEqual(ca[4], 'Balears; Illes')
        self.assertEqual(ca[5], 'Canarias')
        self.assertEqual(ca[17], 'Rioja; La')
    
    def test_aprobados_pau(self):
        aprobados = aprobados_pau(csv)
        self.assertEqual(10103, aprobados['Canarias'])
        self.assertEqual(10497, aprobados['Galicia'])
        self.assertEqual(8648, aprobados['Castilla - La Mancha'])
        self.assertEqual(23536, aprobados['Comunitat Valenciana'])
    
    def test_suspensos_pau(self):
        self.assertEqual(736, suspensos_pau('tests/pcaxis637310428.csv',
                                            'Extremadura'))
        self.assertEqual(1061, suspensos_pau('tests/pcaxis637310428.csv',
                                             'Canarias'))

    def test_comunidad_mas_aprobados(self):
        self.assertEqual('Rioja; La',
                         comunidad_mas_aprobados('tests/pcaxis637310428.csv'))
    
    def test_comunidad_mas_diferencia(self):
        pass



