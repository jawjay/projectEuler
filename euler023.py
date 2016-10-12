from functools import reduce
def factors(n):  
        """
        http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
        """  
        return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
def euler023(N,toget):
    
    class abundantSum:
        def __init__(self,a):
            self.ab = getAbundant(a)
            self.sms = [False]*a
            self.a = a
            self.checksms()

        def abSum(self,n):
            # check if 2 abundant numbers  can sum to n
            for y in (x for x in self.ab if x<= int(n/2)):
                for x in self.ab[::-1]:
                    if (x+y)==n:
                        return True
                    if (x+y) <n:
                        break
            return False

        def checksms(self):

            for i,a in enumerate(self.ab):
                for j in self.ab[a:]:
                    if (i+j)<a:
                        self.sms[i+j] = True
    

    def factors(n):  
        """
        http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
        """  
        return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    def getAbundant(N):
        return [n for n in range(1,N) if (sum(factors(n))-n) > n ]#and len(factors(n))%2==0]
        pass


    abs = abundantSum(N)

    for i in toget:
        if  abs.sms[i]:
            print("YES")
            continue
        print("NO")


    return abs.ab



toget = [24,25,25]
euler023(100000,toget)
