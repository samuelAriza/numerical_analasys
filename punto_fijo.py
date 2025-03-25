import math
from prettytable import PrettyTable

def f(x):
    return x * math.exp(x) - x**2 - 5*x - 3


def g(x):
    return (x * math.exp(x) - x**2 - 3)/5

table = PrettyTable()
table.field_names = ["n","xn", "f(xn)", "ε"]
tolerancia = 5e-5
xa = -0.5
niter = 100

fx = f(xa)
contador = 0
error = tolerancia + 1

table.add_row([contador, xa, f'{fx:4e}', 0])
while fx != 0 and error > tolerancia and contador < niter:
    xn = g(xa)
    fx = f(xn)
    error = abs(xn - xa)
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