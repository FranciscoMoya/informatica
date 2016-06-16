# encoding: utf-8
from __future__ import print_function
import unittest, sys
from .manual import *

class Test_TG(unittest.TestCase):

    def test_manual(self):
        m = ManualGrading('TRABAJO EN GRUPO')
        m.add('TOTAL',
              [m.add('Corrección funcional',
                     [m.new('Descarga de archivos', 2.5),
                      m.new('Procesamiento XML', 2.5),
                      m.new('Generación de gráficas', 2.5)]),
               m.add('Tratamiento de excepciones',
                     [m.new('Errores de comunicación', .5),
                      m.new('Errores en datos y archivos', .5)]),
               m.add('Estructura del programa',
                     [m.new('Divide y vencerás', .5),
                      m.new('Diseño top-down', .5),
                      m.new('Código limpio', .5)]),
               m.add('Puntos extra',
                     [m.new('Banco de pruebas', 1.)])])
        m.print_output()
        print('\nMáxima calificación posible: {}'.
              format(round(m.total,2)),
              file=sys.stderr)

if __name__ == '__main__':
    Test_TG().test_manual()
