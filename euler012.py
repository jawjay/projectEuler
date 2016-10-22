def triangleNumber(n):
    return (n*(n+1))/2
def getDivisors(n):
    d=0
    if n ==1:
        return 1
    for i in range(1,int(n**0.5)+1):
        # print("i: ",i)
        # print("(n/float(i)): ",n/float(i)) 
        if (n/float(i))%1==0:
            d+=1
    return d*2

def euler012(N):
    """
    Find the first triangle number to have over N divisions
    Triangle Number:
    sum from 1 to n 
    """
    i = 1
    divisors = 0
    divisors = [1]*(int(n**0.5))
    while divisors<=N:
        t = triangleNumber(i)
        divisors = getDivisors(triangleNumber(i))
        i+= 1

    return t

print(list(map(lambda x: triangleNumber(x),range(1,10))))
print(list(map(lambda x: getDivisors(triangleNumber(x)),range(1,10))))

print( euler012(1))
print( euler012(2))
print( euler012(3))
print( euler012(4))