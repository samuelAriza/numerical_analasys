import math
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["n","xn", "f(xn)", "Error"]


def f(x):
    return math.exp(x) - 5*x + 2


print(f(0.5))
print(f(1))
tolerancia = 1e-5
x0 = 0.5
x1 = 1
niter = 100

fx0 = f(x0)
if fx0 == 0:
    print(f'{x0} es una raiz de la ecuacion')
else: 
    fx1 = f(x1)
    cont = 0
    error = tolerancia + 1
    den = fx1 - fx0
    table.add_row([cont, x0,f'{fx0:4e}', 0])
    table.add_row([1, x1,f'{fx1:4e}', 0])
    while error > tolerancia and fx1 != 0 and den != 0 and cont < niter:
        x2 = x1 - ((fx1*(x1 - x0))/den)
        error = abs((x2 - x1)/x2)
        x0 = x1
        fx0 = fx1
        x1 = x2
        fx1 = f(x1)
        den = fx1 - fx0
        cont = cont + 1
        table.add_row([cont + 1, x1,f'{fx1:4e}', f'{error:4e}'])
    if fx1 == 0:
        print(f'{x1} es raiz')
    elif error < tolerancia:
        print(f'{x1} es una aproximacion a una raiz con una tolerancia: {tolerancia}')
    elif den == 0:
        print(f'hay una posible raiz multiple')
    else:
        print(f'fracaso en {niter} iteraciones')

print(table)