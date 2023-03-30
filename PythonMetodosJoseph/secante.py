import math
def secante(X0,X1,funcion,tol,iterMax):
    f = lambda x: eval(funcion)
    sk= X0;
    sk_b= X1;
    k=0;
    while(k<iterMax):
        sk_n= sk - (sk-sk_b)/f(sk)-f(sk_b)
        error = abs(sk_n-sk)
        k +=1
        if (error<tol):
            break
        sk_b = sk
        sk = sk_n
    return sk,k,error
        
