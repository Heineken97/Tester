import math
def exp_t(a,iterMax,tol):
    sk = 0
    k=0
    while(k < iterMax):
        sk_n = sk + pow(a,k)/math.factorial(k)
        error = abs(sk_n - sk)
        if(error < tol):
            break
        sk = sk_n
        k += 1
    return sk,k,error
