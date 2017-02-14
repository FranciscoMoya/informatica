def rango_matriz(A):
    return len([x for x in rref(A) if x != [0]*len(A[0])])

def rref(A):
    from copy import deepcopy
    A=deepcopy(A)
    try:
        for i in range(len(A)):
            reducir_filas(A, i, elegir_pivote(A,i))
    except ZeroRowError: pass
    return A

def reducir_filas(A, i, pv):
    for j in range(i+1, len(A)):
        if A[j][pv] != 0:
            k = - A[j][pv]
            mac(A,j,i,k)

def elegir_pivote(A, i):
    pv, f = min((left_most(fila), i+j) for j,fila in enumerate(A[i:]))
    assert pv >= i, 'No redujo bien en el paso anterior'
    if pv >= len(A[0]):
        raise ZeroRowError('No hay más pivotes')
    xch(A,i,f)
    div(A,i,A[i][pv])
    return pv

def left_most(f):
    for i,x in enumerate(f):
        if x != 0: return i
    return len(f)

def xch(A,i,j):
    if i == j: return
    A[i],A[j] = A[j],A[i]

def div(A,i,k):
    f = A[i]
    for j,x in enumerate(f):
        f[j] = x/k
    
def mac(A,i,j,k):
    a,b = A[i],A[j]
    for n,x in enumerate(b):
        a[n] += x*k

class ZeroRowError(Exception):
    pass

import unittest
class Test(unittest.TestCase):
    def test_1_rango_matriz(self):
        self.assertEqual(3, rango_matriz([[1,0,0], [0,1,0], [0,0,1]]))
        self.assertEqual(2, rango_matriz([[0,0,0], [0,1,0], [1,2,0]]))
        self.assertEqual(2, rango_matriz([[1,0,0], [0,0,1], [0,0,2]]))

    def test_2_lin_solve(self):
        def f(): pass
        self.assertEqual(type(lin_solve), type(f))

    def test_3_inv_matriz(self):
        def f(): pass
        self.assertEqual(type(inv_matriz), type(f))

unittest.main()
