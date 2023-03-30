import numpy as np

def sustitucionHacia_Atras(a,b):
    m = len(b)
    x = np.zeros((m,1))

    for i in range(m-1,-1,-1):
        suma = 0
        for j in range(i+1,m):
            suma += a[i][j]*x[j]
        x[i] = (b[i] - suma) / a[i][i]
    return x

a = [[1, 1, -1, 3], [0, -1, -1, -5], [0, 0, 3, 13], [0, 0, 0, -13]]
b = [4, -7, 13, -13]

sol = sustitucionHacia_Atras(a, b)
print(sol)
