
def get_primes(n):
    sieve = [True]*(n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False]*((n-i*i-1)/(2*i)+1)
    return   (2*i+1 for i in xrange(1,n/2) if sieve[i])
def x_prime(n):
    sieve = [True]*(10*n)
    




class primeSieve:
    def __init__(self,n):
        self.n = n
        self.sieve = [True]*(n/2)
        self.updateSieve()
    def updateSieve(self):
        for i in xrange(3,int(self.n**0.5)+1,2):
            if self.sieve[i/2]:
                self.sieve[i*i/2::i] = [False]*((self.n-i*i-1)/(2*i)+1)
        # 
    def getPrimes(self):
        return   (2*i+1 for i in xrange(1,self.n/2) if self.sieve[i])

# T = int(raw_input().strip())
T = 2
ns = [5,10]
for i in range(T):
    # N = int(raw_input().strip())
    N = ns[i]
    tr = 10000
    
    while sum(1 for x in get_primes(tr))+1 < N:
        tr*=10
    
    trls = list(get_primes(tr))
    
    print "N:",N
    print sum(x for x in get_primes(tr) if x <= N)+2


a = primeSieve(100)
print list(a.getPrimes())
