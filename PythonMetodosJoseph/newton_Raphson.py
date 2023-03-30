from matplotlib import pyplot as plt
import numpy as np
import sympy

def newton_Raphson(X0, funcion, tol, iterMax):
    x = sympy.symbols('x')
    f = sympy.sympify(funcion).subs('x', x)
    sympy.plot(f, (x, -10, 10), xlabel='x', ylabel='f(x)')
    plt.show()
    df = sympy.diff(f, x)
    sK = X0
    k = 0
    while k < iterMax:
        df_val = df.evalf(subs={x: sK})
        if df_val == 0:
            print("Derivada no debe ser cero")
            break
        sK = sK - f.evalf(subs={x: sK}) / df_val
        error = abs(f.evalf(subs={x: sK}))
        k += 1
        if error < tol:
            print("Se ha llegado a la tolerancia maxima")
            break
    if k >= iterMax:
        print("La cantidad de iteraciones llego a su punto maximo")
    return sK.evalf(), k, error.evalf()

