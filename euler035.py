def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    # return sieve
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def getCombinations(n):
    s = list(n)
    ot = []
    for i in range(len(s)):
        ot.append(''.join(s[i:]+s[:i]))
    return ot

def euler035(N):
    primes = rwh_primes1(1000000)
    sieve = [False]*1000000
    ot = 0
    for p in primes:
        sieve[p] = True
    for i in range(1,1000000-2):
        if not sieve[i]:
            continue
        if all((sieve[int(x)] for x in getCombinations(str(i)))):
            print i
            ot +=1

    print 'sum: ',ot

getCombinations('1234')
# rwh_primes1(1000000)
euler035(1)