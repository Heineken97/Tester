import math
from matplotlib import pyplot as plt
import numpy as np

def falsaPosicion(a,b,funcion,tol,iterMax):
    f = lambda x: eval(funcion)
    plt.title("Funcion a evaluar")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    x = np.linspace(a,b,50)
    plt.plot(x,f(x),"mD")
    k=0
    A=a
    B=b
    while(k<iterMax):
        if(f(A)*f(B)>0):
            print("El teorema de Bolzano no matix")
            break
        X = B - ((B-A)/(f(B)-f(A)))*f(B)
        k +=1
        error = abs(f(X))
        if(error<tol):
            print("Se ha superado la tolerancia maxima")
            break
        if(f(A)*f(X)<0):
            B = X
        else:
            A = X
    if(k>=iterMax):
        print("Se alcanzaron la cantidad maxima de iteraciones")
    return X,k,error
    
