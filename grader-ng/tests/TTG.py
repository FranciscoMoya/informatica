# encoding: utf-8
import unittest, sys
from .manual import *

class Test_TG(unittest.TestCase):

    def test_manual(self):
        agregar('TOTAL',
                [self.correccion_funcional(),
                 self.tratamiento_excepciones(),
                 self.estructura(),
                 self.pruebas()])
        print_output()

    def correccion_funcional(self):
        return agregar('Corrección funcional',
                       [manual('Descarga de archivos', .25),
                        manual('Procesamiento XML', .25),
                        manual('Generación de gráficas', .25)])

    def tratamiento_excepciones(self):
        return agregar('Tratamiento de excepciones',
                       [manual('Errores de comunicación', .05),
                        manual('Errores en datos y archivos', .05)])

    def estructura(self):
        return agregar('Estructura del programa',
                       [manual('Divide y vencerás', .05),
                        manual('Diseño top-down', .05),
                        manual('Código limpio', .05)])
        
    def pruebas(self):
        return agregar('Puntos extra',
                       [manual('Banco de pruebas', .10)])

        
if __name__ == '__main__':
    Test_TG().test_manual()
