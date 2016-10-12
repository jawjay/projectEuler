def euler028(N):
    pass

def sumDiag(N):
    return 1+sum((4*(2*n-1)**2-6*(2*n-2) for n in range(2,N+1)))

print(sumDiag(501))
