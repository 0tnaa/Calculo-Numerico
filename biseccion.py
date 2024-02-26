from math import *

def Biseccion(funcion,a,b,tolerancia,num_iteracion):
	error_aprox = float('inf') #Inicializa el error a infinito
	punto_actual = a
	punto_anterior = b
	contador_iteracion = 1
	if (funcion(a)*funcion(b) > 0):
		print('La funcion no cambia de signo')
	else:
		while (contador_iteracion < num_iteracion and error_aprox > tolerancia):
			punto_anterior = punto_actual
			punto_actual = (a+b)/2
			if(funcion(a)*funcion(punto_actual) < 0): #cambia de signo en el intervalo [a,m]
				b = punto_actual
			if(funcion(punto_actual)*funcion(b) < 0): #cambia de signo en el intervalo [m,b]
				a = punto_actual
			error_aprox = abs((punto_actual-punto_anterior)/punto_actual)
			print('\nIteraccion',contador_iteracion,'intervalo: [',a,',',b,']')
			contador_iteracion = contador_iteracion + 1
		print('\nSolucion en m(',contador_iteracion-1,') =',punto_actual,'\n')
		print('Error relativo: ',error_aprox)

if __name__ == '__main__':
	f = lambda x: sin (x) - e**-x #funcion 
	# otro ejercicio sin (x) - e**-x 0 1
	# otro ejercicio e**x - 3*x**2 0 1
	a = 0 # intervalo a
	b = 1 # intervalo B
	tol = 0.03 
	ni = 50 # Numero de iteracciones
	Biseccion(f, 0, 1, 0.03, ni)
