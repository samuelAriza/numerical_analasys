import math
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["i","xinf", "xsup", "xm", "f(xmi)", "error"]

xi = 2 
xs = 3
tolerancia = 0.5e-3
niter = 100

def f(x):
    return math.exp(3*x - 12) + x * math.cos(3*x) - x**2 + 4

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
    while error > tolerancia and fxm != 0 and contador < niter:
        if fxi*fxm < 0:
            xs = xm
            fxs = f(xm)
        else:
            xi = xm
            fxi = f(xm)
        xaux = xm
        xm = (xi + xs)/2
        fxm = f(xm)
        error = abs(xm - xaux)
        contador = contador + 1
        table.add_row([contador, xi, xs, xm, f'{fxm:4e}', f'{error:4e}'])

    if fxm == 0:
        print(f'{xm} es raiz')
    elif error < tolerancia:
        print(f'{xm} es aproximacion a una raiz con una tolerancia de {tolerancia}')
    else:
        print(f'Fracaso en {niter} iteraciones')
else:
    print("Intervalo inadecuado")

print(table)