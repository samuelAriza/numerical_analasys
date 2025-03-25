import math

def f(x):
    return math.exp(3*x - 12) + x * math.cos(3*x) - x**2 + 4

#Args
x0 = -10
delta = 1
niter = 16

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
