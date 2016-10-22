#Smallest Multiple
	#What is the smallest positive number that is evenly divisible(divisible with no remainder) 
	#by all of the numbers from 1 to N
#T = int(raw_input().strip())

    
N = 10

nums = range(1,N+1)[::-1]
def euler0052(h):
    nums = [20,19,18,17,16,15,14,13,12,11]
    N = 10000
    factor_sieve = [0]*N
    for x in nums:
        val = x
        while val<N:
            factor_sieve[val]+=1
            val+=x
    for i,a in enumerate(factor_sieve):
        if a==10:
            return i
def euler005(N):
    nums = range(11,20)
    factor_sieve = [0]*N
    for x in nums:
        val = x
        while val<N:
            factor_sieve[val]+=1
            val+=x
    ns = [x for x in factor_sieve if x>8]
    print(ns)
