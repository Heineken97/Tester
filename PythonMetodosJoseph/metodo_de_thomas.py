import numpy as np

def metodo_de_thomas(A, d):
    # Paso 1: Crear matriz A y vector d
    n = len(d)
    a = np.concatenate(([0], np.diag(A, -1)))
    b = np.diag(A, 0)
    c = np.concatenate((np.diag(A, 1), [0]))
    x = np.zeros((n, 1))

    # Paso 3: Calcular vectores p y q
    p = np.zeros((n-1, 1))
    q = np.zeros((n, 1))
    p[0] = c[0] / b[0]
    q[0] = d[0] / b[0]

    for i in range(1, n-1):
        if abs(b[i] - p[i-1] * a[i]) < 1e-15:
            a[i] += 1e-15
        p[i] = c[i] / (b[i] - p[i-1] * a[i])
        q[i] = (d[i] - q[i-1] * a[i]) / (b[i] - p[i-1] * a[i])

    if abs(b[n-1] - p[n-2] * a[n-1]) < 1e-15:
        a[n-1] += 1e-15
    q[n-1] = (d[n-1] - q[n-2] * a[n-1]) / (b[n-1] - p[n-2] * a[n-1])

    # Paso 4: Calcular vector solución x
    x[n-1] = q[n-1]

    for i in range(n-2, -1, -1):
        x[i] = q[i] - p[i] * x[i+1]

    return x

def matriz_tridiagonal(m):
    a = np.full((m,), 5)
    b = np.full((m-1,), 1)
    A = np.diag(a) + np.diag(b, 1) + np.diag(b, -1)
    return A

n = 100
A = matriz_tridiagonal(n)
d = np.array([-12] + [-10]*(n-2) + [-12]).reshape((n,1))

# Llamar al método de Thomas
x = metodo_de_thomas(A, d)
print(x)



