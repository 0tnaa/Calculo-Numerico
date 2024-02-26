def f(x):
    return sqrt(x+1)

def trapecio(funcion,a, b, n):
    h = (b - a) / n
    suma = 0.5 * (funcion(a) + funcion(b))
    for i in range(1, n):
        x =a+i*h
        suma += funcion(x)
    return h * suma
