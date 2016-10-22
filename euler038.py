from euler024 import lexPerm

def unique(s):
    return len(set(s)) == len(s)

def euler038(N):
    pan = set((str(x) for x in range(1,10)))
    for i in range(9999,10,-1):
        n = 2
        if not unique(str(i)+str(2*i)):
            continue
        mset = set(str(i)+str(i*2))
        while len(mset)<9:
            n+= 1
            ns = str(n*i)
            if not unique(ns):
                break
            if mset.intersection(set(ns)):
                break
            mset = mset.union(set(ns))
        if mset==pan:
            print (i)
            return [str(i*x) for x in range(1,n+1)]
    print(i,n)

print euler038(0)
# i = 192
# print unique(str(i)+str(2*i))
# print[ 987654312%x for x in [3,6,10,15,21,28]]
# n = range(1,4)

