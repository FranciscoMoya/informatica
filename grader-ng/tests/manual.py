# encoding: utf-8
from __future__ import print_function
from builtins import input
import sys

class ManualGrading(object):
    def __init__(self, title):
        self._items=title
        self._comment=''
        self._total=0.

    def input_grade(self, item, points):
        while True:
            # El funcionamiento de input(prompt) es muy extraño:
            # - Si stderr se redirige el prompt va a stderr
            # - En caso contrario el prompt va a stdout
            try:
                print('{} ({}): '.format(item, points), end='')
                grade = float(input())
            except EOFError: raise
            except:          continue
            print('Comentario para {}: '.format(item))
            self._comment += input()
            if grade <= points:
                return grade
            print('Debe ser <= {}'.format(points))

    def new(self, item, points):
        grade = self.input_grade(item, points)
        self._items += '\n  {} {}'.format(grade, item)
        self._total += points
        return grade

    def add(self, item, list):
        grade = round(sum(list),2)
        self._items += '\n{} {}'.format(grade, item)
        return grade

    def print_output(self):
        print(self._items, file=sys.stderr)
        print('-'*70, file=sys.stderr)
        print(self._comment, file=sys.stderr)

    @property
    def total(self):
        return self._total
