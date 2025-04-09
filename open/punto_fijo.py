import math
from prettytable import PrettyTable

'''
Punto fijo 
'''

def f(x):
    return (1/x) + (0.4) -(1.74*math.log(50*math.sqrt(x)))

def g(x):
    return 1/(-0.4 + 1.74*math.log(50*math.sqrt(x)))

table = PrettyTable()
table.field_names = ["n","xn", "f(xn)", "ε"]
tolerancia = 5e-3
xa = 0.5
niter = 1000

fx = f(xa)
contador = 0
error = tolerancia + 1

table.add_row([contador, xa, f'{fx:4e}', 0])
while fx != 0 and error > tolerancia and contador < niter:
    xn = g(xa)
    fx = f(xn)
    error = abs((xn - xa)/xn)
    xa = xn
    contador = contador + 1
    table.add_row([contador, xa, f'{fx:4e}', f'{error:4e}'])
if fx == 0:
    print(f'{xa} es raiz')
elif error < tolerancia:
    print(f'{xa} es una aproximacion con una tolernacia = {tolerancia}')
else:
    print("fracaso")

print(table)


'''
Biseccion
'''

table = PrettyTable()
table.field_names = ["i","xinf", "xsup", "xm", "f(xmi)", "error"]

xi = 0.05
xs = 2
tolerancia = 5e-3
niter = 100

print(f(2))

fxi = f(xi) 
fxs = f(xs) 
if fxi == 0:
    print(f'{xi} es raiz')
elif fxs == 0:
    print(f'{xs} es raiz')
elif fxi*fxs < 0:
    xm = (xi + xs)/2
    fxm = f(xm)
    contador = 1
    error = tolerancia + 1
    
    table.add_row([contador, xi, xs, xm, f'{fxm:4e}', 0])
    while abs(fxm) > 1e-4 and error > tolerancia and fxm != 0 and contador < niter:
        if fxi*fxm < 0:
            xs = xm
            fxs = f(xm)
        else:
            xi = xm
            fxi = f(xm)
        xaux = xm
        xm = (xi + xs)/2
        fxm = f(xm)
        error = abs((xm - xaux)/xm)
        contador = contador + 1
        table.add_row([contador, xi, xs, xm, f'{fxm:4e}', f'{error:4e}'])

    if fxm == 0:
        print(f'{xm} es raiz')
    elif abs(fxm) < 1e-4:
        print(f'Yalupa {xm}')
    elif error < tolerancia:
        print(f'{xm} es aproximacion a una raiz con una tolerancia de {tolerancia}')
    else:
        print(f'Fracaso en {niter} iteraciones')
else:
    print("Intervalo inadecuado")

print(table)