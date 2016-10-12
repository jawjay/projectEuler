
def multSum(K):
    N = 1
    for i in K:
        N*=i
    return N

def largestProd(N,K,num):
    mx = 0
    for i in range(N-K+2):
        # i is starting index for range
        print("[",i,":",i+K-1,"]")
        p = multSum(map(lambda x:int(x),list(num[i:i+K])))
        mx = max(mx,p)
    return mx


print largestProd(10,5,'3675356291')
print multSum([1,2,3])

