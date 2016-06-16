from __future__ import print_function
from builtins import input
import sys

__ttg_output=''

def input_grade(item, points):
    while True:
        print(item + ': ', end='')
        try:
            grade = float(input())
        except EOFError:
            raise
        except:
            continue
        if grade <= points:
            return grade
        print('Debe ser <= {}'.format(points))

def manual(item, points):
    global __ttg_output
    grade = input_grade(item, points)
    __ttg_output += '\n  {} {}'.format(grade, item)
    return grade

def agregar(item, list):
    global __ttg_output
    grade = round(sum(list),2)
    __ttg_output += '\n{} {}'.format(grade, item)
    return grade

def print_output():
    global __ttg_output
    print(__ttg_output, file=sys.stderr)
