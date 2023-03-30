import numpy as np

def sol_jacobi(A, b, x0, iterMax, tol):
    xk = x0
    #P1:
    d = np.diag(A) #Vector diagonal
    D = np.diag(d) #Matriz diagonal
    #P2:
    LmU = A - D
    #P3:
    d_in = 1 / d #Vector con inverso multiplicativo de d
    D_in = np.diag(d_in) #La inversa de D
    #P4:
    z = D_in @ b
    M = -D_in @ LmU
    #P5
    for k in range(1, iterMax+1):
        #P5.1
        xk = M @ xk + z
        #P5.2
        error = np.linalg.norm(A @ xk - b)
        #P5.3
        if error < tol:
            break
    return xk, k, error

# Ejemplo de prueba
A = np.array([[10, -1, 2], [-1, 11, -1], [2, -1, 10]])
b = np.array([6, 25, -11])
x0 = np.zeros_like(b)
iterMax = 100
tol = 1e-6

sol, k, error = sol_jacobi(A, b, x0, iterMax, tol)
print("Solución: ", sol)
print("Iteraciones: ", k)
print("Error: ", error)
