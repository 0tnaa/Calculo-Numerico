def f(x):
    return sqrt(x+1)

def suma_riemann(funcion,a,b,n):
    h = (b-a)/n
    acum = 0
    for i in range (n):
        x = a+i*h
        acum = acum+h*funcion(x)
    return acum
