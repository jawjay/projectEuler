import math

def binet(n):
    m5 = math.sqrt(5)
    return (1/m5)   *(((1+m5)/2)**n-((1-m5)/2)**n)
def euler025(N):
    # need binets fib formula to get large numbers

    # fn1 = 1
    # fn2 = 1
    # ind = 2
    # while len(str(fn2)) != N:
    #     fn1,fn2 = fn2,fn1+fn2
    #     ind+=1
    # return ind
    at = 2
    fn2 = binet(at)
    sl = len(str(fn2))
    while sl <= N:
        at *= 2 
        fn2 = binet(at)
        sl = len(str(fn2))
    print(at)
# print(euler025(1000))
for i in range(100):
    print(len(str(binet(i))))