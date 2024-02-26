import unittest
import biseccion
import newton_raphson
import riemann
import trapecio

from math import *

def f(x):
    return sqrt(x+1)

def f2(t, y):
   return (t-y)**2+1

class test_biseccion(unittest.TestCase):
    def test_biseccion(self):
        funcion = lambda x: e**x - 3*x**2
        a = 0
        b = 1
        tolerancia = 0.02
        num_iteracion = 100
        self.assertEqual(biseccion.Biseccion(funcion,a,b,tolerancia,num_iteracion),None)

class test_newton_raphson(unittest.TestCase):
    def test_newton_raphson(self):
        f= lambda x: e**x-3*x**2 
        df = lambda x: e**x-6*x  
        x0 = 0.7  #valor inicial de x
        tol = 0.02 #margen
        self.assertEqual(newton_raphson.newthon_raphson(f,df,x0,tol),0.9100079800667897)

class test_riemann(unittest.TestCase):
    def test_suma_riemann(self):
        a = -1  # inicio del intervalo
        b = 1   # fin del intervalo
        n = 5   # numero de participaciones
        self.assertEqual(riemann.suma_riemann(f, a, b, n),1.5548955608445105)
                         
class test_trapecio(unittest.TestCase):
    def test_trapecio(self):
        a = -1
        b = 1
        n = 5
        self.assertEqual(trapecio.trapecio(f, a, b, n),1.8377382733191294)

if __name__ == "__main__":
    unittest.main()
