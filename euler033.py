import math
def factors(n):  
        """
        http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
        """  
        return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def prod(N):
    x = 1
    for n in N:
        x *= n
    return x
def euler033(N):
    # pass

    fracs = []
    for i in range(11,100):
        for j in range(11,100):
            si = set(str(i))
            sj = set(str(j))
            if len(si.intersection(sj))==1 and len(si.union(sj))==3:
                c = list(si.intersection(sj))[0] # comon number
                si = str(i).replace(c,"")
                sj = str(j).replace(c,"")
                # print(si,sj)
                if i/j>1:
                    continue
                if int(sj)==0 or j==0:
                    continue
                if (1.0*i)/(1.0*j)==(1.0*int(si))/(1.0*int(sj)) :
                    if i%10!=0 and j%10!=0:
                        # print(i,j)                # print(i,j)
                        fracs.append((i,j))
    # print(fracs)
    zf = (zip(*fracs))
    num = zf[0]
    den = zf[1]
    # print(num,den)
    c = (prod(num),prod(den))
    # print c
    m = (max(list( set(factors(c[0]).intersection(set(factors(c[1])))))))
    # print m
    return c[1]/m
    # print(c)
euler033(1)