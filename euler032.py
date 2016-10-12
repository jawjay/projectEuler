import math
def euler032(n):
    lb = 0
    ub = 10000
    ot = []
    rst = set(list([str(x) for x in range(1,n+1)]))
    for i in range(lb,ub):
        for j in range(lb,ub):
            if len(str(i)+str(j)+str(i*j))>n:
                break
            if set(str(i)+str(j)+str(i*j)) == rst:
                print(i,j,i*j)
                ot.append(i*j)

    print(sum(set(ot)))
    # print(high)
euler032(9)