import math
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["i","xinf", "xsup", "xm", "f(xmi)", "error"]

xi = 0.05
xs = 2
tolerancia = 0.5e-100
niter = 100

def f(x):
    return 1/x + 0.4 - 1.74*math.log10(169-math.sqrt(x))

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