import numpy as np

def pseudoinversa(A,B,tol,iterMax):
    alpha = np.linalg.norm(A, 'fro')
    X = (1.0/alpha**2)*np.array(A)
    for k in range(1, iterMax+1):
        X = X@(2*np.eye(np.shape(A)[0])-A@X)
        error = np.linalg.norm(A@X@A-A, 'fro')
        if error<tol:
            break
    pInv = X
    x = X@B

    error = np.linalg.norm(A@x-B)
    return X,error,k
