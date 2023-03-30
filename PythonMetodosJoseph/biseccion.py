import math
from matplotlib import pyplot as plt
import numpy as np

def biseccion(a,b,funcion,iterMax,tol):
    f = lambda x: eval(funcion)
    plt.title("Funcion a Evaluar")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    x = np.linspace(a,b,100)
    plt.plot(x,f(x),'mD')
    plt.show()
    sk=0
    k=0
    error = 0
    if (f(a)*f(b)<= 0):
        while(k < iterMax):
            sk = (a+b)/2
            if (f(a)*f(sk) < 0):
                b = sk
            elif(f(b)*f(sk) < 0):
                a = sk
            else:
               print("No se cumple Teorema de bolzano de dentro de while")
            error = abs(f(sk))
            k += 1
            if(error<tol):
                print("El error alcanzo el limite de la tolerancia")
                break
    else:
        print("El intervalo inicial no cumple con Teorema de Bolzano")
    if(k>=iterMax):
        print("El numero maximo de iteraciones se ha sobrepasado")
    return sk,k,error
   
            

