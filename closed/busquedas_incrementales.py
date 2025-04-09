import math

def f(x):
    return x**3 - (1/math.sqrt(2))*(x**2) - 5*x


#Argumentos
x0 = -4
delta = 1
niter = 20

if f(x0) == 0:
    print(f'{x0} es raiz')
else:
    x1 = x0 + delta
    contador = 1
    while (f(x0)*f(x1) > 0 and contador < niter):
        x0 = x1
        x1 = x0 + delta
        contador = contador + 1
    if f(x1) == 0:
        print(f'{x1} es raiz')
    elif(f(x0)*f(x1) < 0):
        print(f'Hay una raiz entre {x0} y {x1}')
    else:
        print("Fracaso")
