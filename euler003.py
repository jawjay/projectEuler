# largest prime factor of given number N

#T = int(raw_input().strip())
def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    n = int(n)
    sieve = [True] * int(n/2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * int((n-i*i-1)/(2*i)+1)
    # return sieve
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]


N = 600851475143
primes = rwh_primes1(int(N**0.5))
for p in primes[::-1]:
    if N%p==0:
        print(p)
        break

