import numpy as np

def sustitucionHacia_Adelante(a,b):
    m = len(b)
    x = np.zeros(m)

    for i in range(m):
        suma = 0
        for j in range(i):
            suma = suma + a[i,j]*x[j]
        x[i] = (b[i] - suma) / a[i, i]
    return x

a = np.array([[3, 0, 0], [2, -3, 0], [-1, 4, 5]])
b = np.array([4, -7, 13])

sol = sustitucionHacia_Adelante(a, b)

print(sol)
