from math import  *

def f(x):
    return e**x-3*x**2 #  sin(x) - e**-x 

def df(x):
    return e**x-6*x #  cos(x) + e**-x

def newthon_raphson(f, df, x0, tolerancia, max_iteracion=1000):
    i = 0
    error_aprox = float('inf') #Inicializa el error a infinito
    print ("| i | xi | xi+1 | error |")
    print ("-------------------------")
    while (i < max_iteracion and error_aprox > tolerancia):
        x1 = x0 - f(x0) / df(x0)
        if i > 0: # Calculo del error relativo a partir de segunda iteracion
            error_aprox = abs(x1 - x0) / abs(x1)
        print ('|',i, '|', x0, '|','|',x1, '|',error_aprox,'|')
        if abs(x1 - x0) < tolerancia * abs(x1):
            return x1
        x0 = x1
        i += 1
    raise ValueError("El método de Newton-Raphson no converge después de %d iteraciones." % max_iteracion)
