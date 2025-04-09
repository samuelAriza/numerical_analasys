import math
from prettytable import PrettyTable

'''
Neston
'''

def f(x):
    return (1/x) + (0.4) -(1.74*math.log(50*math.sqrt(x)))

'''Derivada de f'''
def defx(x):
    return 1/(-0.4 + 1.74*math.log(50*math.sqrt(x)))

table = PrettyTable()
table.field_names = ["n","xn", "f(xn)", "dfx(xn)", "ε"]

tolerancia = 5e-3
xa = 0.5
niter = 1000

fx = f(xa)
dfx = defx(xa)
contador = 0
error = tolerancia + 1

table.add_row([contador, xa, f'{fx:4e}', 0])
while fx != 0 and error > tolerancia and dfx != 0 and contador < niter:
    x1 = xa - (fx/dfx)
    fx = f(x1)
    dfx = defx(x1)
    error = abs((xn - xa)/xn)
    xa = x1
    contador = contador + 1
    table.add_row([contador, xa, f'{fx:4e}', f'{dfx:4e}' f'{error:4e}'])
if fx == 0:
    print(f'{xa} es raiz')
elif error < tolerancia:
    print(f'{xa} es una aproximacion con una tolernacia = {tolerancia}')
elif dfx == 0:
    print(f'{xa} es una posible raiz multiple')
else:
    print("fracaso")

print(table)