def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    # return sieve
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]



def euler037(N):
    primes = rwh_primes1(N)
    sieve = [False]*N
    for p in primes:
        sieve[p] = True
    lt = lambda x: [x[i:] for i in range(len(x))]
    rt = lambda x: [x[:i+1] for i in range(len(x))][::-1]
    sm = 0
    for i in range(10,N):
        if not sieve[i]:
            continue
        if all ( sieve[int(x)] for x in (lt(str(i)) + rt(str(i)))  ):
            # print i
            sm += i
    print sm
euler037(1000000)