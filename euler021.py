from functools import reduce
def sumLess(st,a):
    sm = 0
    for i in st:
        if i <= a:
            sm+=i

    return sm
def factors(n):  
    """
    http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    """  
    return list(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def euler021(N):

    class amicable:
        def __init__(self,n):
            self.nums = [0]*(2*n+1)
        def setNum(self,n):
            if n>=len(self.nums):
                return
            if self.nums[n]==0:
                self.nums[n] = sum(factors(n))-n
        def getNum(self,n):
            if n >=len(self.nums):
                return -1
            return self.nums[n]


    am = set()
    nums = amicable(N)
    for i in range(1,N):
        nums.setNum(i)
        a = nums.nums[i]
        nums.setNum(a)
        if i == nums.getNum(a) and i!=a:
            am.add(i)
            am.add(a)
    return sum(am)
    pass





print((euler021(10000)))
